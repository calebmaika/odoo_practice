from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ErpJournalEntry(models.Model):
    """
    Journal Entry Model (Header)
    
    This represents a single accounting transaction.
    Think of it as a "container" that holds multiple journal items (lines).
    
    In standard Odoo, this would be 'account.move', but we're creating
    a custom version for learning purposes.
    """
    _name = 'erp.journal.entry'
    _description = 'Journal Entry'
    _order = 'date desc, id desc'

    name = fields.Char(string = 'Reference', required = True, default = '/')
    date = fields.Date(string = 'Date', default = fields.Date.context_today, required = True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted')
    ], string = 'Status', default = 'draft', required = True, readonly = True)
    line_ids = fields.One2many('erp.journal.item', 'entry_id', string = 'Entry Lines')

    def action_post(self):
        for record in self:
            # Validation 1: Must have at least 2 lines
            # Double-entry bookkeeping requires at least one debit and one credit
            if len(record.line_ids) < 2:
                raise ValidationError(_(
                    "A journal entry must have at least 2 lines!\n"
                    "Double-entry bookkeeping requires at least one debit and one credit."
                ))
            
            # Validation 2: Calculate totals
            # .mapped('debit'): Gets all debit values from lines
            # sum(): Adds them together
            total_debits = sum(record.line_ids.mapped('debit'))
            total_credits = sum(record.line_ids.mapped('credit'))

            # Validation 3: Check if balanced
            # In accounting, debits MUST equal credits
            # We use a small tolerance (0.01) to handle floating-point rounding errors
            if abs(total_debits - total_credits) > 0.01:
                raise ValidationError(_(
                    "Journal entry is not balance!\n"
                    "Total Devits: %(debits).2f\n"
                    "Total Credits: %(credits).2f\n"
                    "Difference: %(deff).2f\n\n"
                    "Debits and Credits must be equal before posting."
                )% {
                    'debits': total_debits,
                    'credits': total_credits,
                    'diff': abs(total_debits - total_credits)
                })
            
            # Validation 4: Each line must have either debit OR credit (not both, not neither)
            for line in record.line_ids:
                has_debit = bool(line.debit and line.debit != 0)
                has_credit = bool(line.credit and line.credit != 0)

                if has_debit and has_credit:
                    raise ValidationError(_(
                        "Line '%(label)s' has both debit and credit amounts!\n"
                        "Each line must have either a debit OR a credit, not both."
                    )% {'label': line.label or 'Untitled'})

                if not has_debit and not has_credit:
                    raise ValidationError(_(
                        "Line '%(label)s' has no debit or credit amount!\n"
                        "Each line mumst have either a debit or a credit."
                    )% {'label': line.label or 'Untitled'})

            # All validations passed - change state to posted
            # This locks the entry from further editing
            record.state = 'posted'

        return True
    
    def action_draft(self):
        for record in self:
            record.state = 'draft'
        return True
    
class ErpJournalItem(models.Model):
    """
    Journal Item Model (Lines)
    
    This represents a single line in a journal entry.
    Each line records one debit or credit to a specific account.
    
    In standard Odoo, this would be 'account.move.line'.
    """

    _name = 'erp.journal.item'
    _description = 'Journal Item'
    _order = 'entry_id, id'

    # date = fields.Date(
    #     string - 'Date',
    #     related = 'entry_id.date',
    #     store = False,
    #     readonly = True,
    # )

    entry_id = fields.Many2one(
        'erp.journal.entry',
        string = 'Entry',
        required = True,
        ondelete = 'cascade',
        index = True
    )

    account_id = fields.Many2one(
        'erp.account',
        string = 'Account',
        required = True,
        index = True
    )

    debit = fields.Float(string = 'Debit', default = 0.0)
    credit = fields.Float(string = 'Credit', default = 0.0)
    label = fields.Char(string = 'Label', required = True)

    account_balance = fields.Float(
        string = 'Account Balance',
        related = 'account_id.balance',
        readonly = True
    )

    account_code = fields.Char (
        string = 'Account Code',
        related = 'account_id.code',
        readonly = True
    )

    #CONSTRAINTS
    @api.constrains('debit', 'credit')
    def _check_debit_credit(self):
        """
        Constraint: A line cannot have both debit and credit.
        
        This is a database-level validation that runs automatically
        when records are created or updated.
        
        @api.constrains: Decorator that triggers validation
        """
        for record in self:
            #check if both debit and credit have values
            if record.debit and record.credit:
                raise ValidationError(_(
                    "A journal item cannot have both debit and credit amounts!\n"
                    "Line: %(label)s\n"
                    "Please enter either a debit OR a credit, not both."
                )% {'label': record.label or 'Untitled'})

            #check if neither has value
            if not record.debit and not record.credit:
                raise ValidationError(_(
                    "A journal item must have either a debit or credit amount!\n"
                    "Line: %(label)s\n"
                    "Please enter either a debit or a credit amount."
                ) % {'label': record.label or 'Untitled'})