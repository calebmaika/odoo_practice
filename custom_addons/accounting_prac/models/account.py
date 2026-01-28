from odoo import models, fields, api

class ErpAccount(models.Model):
    _name = 'erp.account'
    _description = 'Accounting Account'
    _order = 'code'

    #FIELDS
    name = fields.Char(string = 'Account Name', required = True)
    code = fields.Char(string = 'Code', required = True)
    account_type = fields.Selection([
        ('asset', 'Asset'),
        ('liability', 'Liabiility'),
        ('equity', 'Equity'),
        ('income', 'Income'),
        ('income', 'Income'),
        ('expense', 'Expense')
    ], string = 'Type', required = True)

    balance = fields.Float(string = 'Current Balance', compute = '_compute_balance', store = True)
    item_ids = fields.One2many('erp.journal.item', 'account_id', string = 'Journal Items')

    @api.depends('item_ids.debit', 'item_ids.credit')
    def _compute_balance(self):
        for record in self:
            items = record.item_ids
            total_debits = sum(items.mapped('debit'))
            total_credits = sum(items.mapped('credit'))

            record.balance = total_debits - total_credits