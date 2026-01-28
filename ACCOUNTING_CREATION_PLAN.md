# Accounting System Creation Plan (From Scratch)

This plan outlines the step-by-step creation of a core Accounting module within your ERP system. We will follow Odoo's architectural patterns to ensure scalability and integration.

**Location:** `custom_addons/erp-system/src/modules/accounting`

**Full Absolute Path:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting`

---

## 📖 The Concept: How Accounting Works in an ERP

### Understanding Double-Entry Bookkeeping

Accounting is based on **Double-Entry Bookkeeping**. This fundamental principle states that every financial transaction must have at least one Debit and one Credit that balance to zero. Think of it like a scale - if you add weight (debit) to one side, you must add equal weight (credit) to the other side to keep it balanced.

**Example Transaction:**
- You receive $1,000 cash from a customer for a sale
- **Debit:** Cash Account (+$1,000) - Money coming IN
- **Credit:** Sales Revenue Account (+$1,000) - Income earned
- **Result:** Both sides equal $1,000, transaction is balanced ✓

### What We Will Build

1.  **Chart of Accounts:** The list of "buckets" where money is tracked.
    - Think of this as a filing cabinet with labeled drawers
    - Each account has a unique code (e.g., 1000 = Cash, 4000 = Sales)
    - Accounts are categorized by type: Asset, Liability, Equity, Income, Expense

2.  **Journal Entries:** The "records" of transactions.
    - This is like a diary entry for each business transaction
    - Contains: Date, Reference Number, Description
    - Can be in Draft (editable) or Posted (locked) state

3.  **Journal Items:** The individual "lines" (Debits/Credits) inside an entry.
    - These are the actual debit/credit lines that make up a journal entry
    - Each line references an Account and has either a Debit OR Credit amount
    - Multiple lines together must balance (total debits = total credits)

---

## 🛠️ Phase 1: Module Scaffolding
Setting up the structure so Odoo recognizes your code.

### 📝 Checklist
- [ ] Create directory: `custom_addons/erp-system/src/modules/accounting/models`
- [ ] Create directory: `custom_addons/erp-system/src/modules/accounting/views`
- [ ] Create directory: `custom_addons/erp-system/src/modules/accounting/security`
- [ ] Create `__init__.py` (Top-level and in `models/`)
- [ ] Create `__manifest__.py`

### 📁 Complete Directory Structure

After creating all folders, your structure should look like this:

```
c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\
│
├── __init__.py                    # Top-level init file (imports models)
├── __manifest__.py                # Module definition file (REQUIRED)
│
├── models\                         # Python model files (database tables)
│   ├── __init__.py                # Models init (imports all model classes)
│   ├── account.py                 # Chart of Accounts model
│   └── journal_entry.py          # Journal Entry and Item models
│
├── views\                         # XML view definitions (user interface)
│   ├── account_menus.xml          # Menu structure for Accounting
│   ├── account_views.xml          # List/Form views for Accounts
│   └── journal_views.xml          # List/Form/Kanban views for Journal Entries
│
└── security\                      # Access control files
    └── ir.model.access.csv        # Permission rules (who can read/write)
```

### 💡 Why This Structure?

**Odoo Module Architecture Explained:**

1. **`__manifest__.py`** - This is the "ID card" of your module. Odoo reads this file first to:
   - Know the module exists
   - Understand what other modules it depends on
   - Know which files to load (security, views, data)
   - Display module info in the Apps menu

2. **`models/`** - Contains Python classes that define database tables. Each `.py` file typically contains one or more model classes. Odoo automatically creates database tables based on these models.

3. **`views/`** - Contains XML files that define the user interface. These tell Odoo:
   - What fields to show in forms
   - How to display lists
   - What menus to create
   - Button actions and workflows

4. **`security/`** - Contains access control rules. Without proper security rules, even if you create models, users won't be able to see or use them.

5. **`__init__.py`** files - Python requires these to treat directories as packages. They also serve as import points for your code.

### 💻 Code Example: `__manifest__.py`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\__manifest__.py`

```python
{
    # Display name shown in Odoo Apps menu
    'name': 'Custom ERP Accounting',
    
    # Version number (use semantic versioning: major.minor.patch)
    'version': '1.0',
    
    # Short description shown in module list
    'summary': 'Core Accounting Module for ERP',
    
    # Detailed description (can be multi-line string)
    'description': 'Handles Chart of Accounts, Journal Entries, and Financial Reporting.',
    
    # Category determines where module appears in Apps menu
    # Options: Accounting, Sales, Inventory, etc.
    'category': 'Accounting',
    
    # Your name or company name
    'author': 'Your Name',
    
    # List of modules this module depends on
    # 'base' is always required - it provides core Odoo functionality
    'depends': ['base'],
    
    # List of data files to load when module is installed
    # Order matters! Security must load before views that reference it
    'data': [
        'security/ir.model.access.csv',  # Load security rules first
        'views/account_menus.xml',       # Then menus
        'views/account_views.xml',       # Then account views
        'views/journal_views.xml',       # Finally journal views
    ],
    
    # Must be True for module to be installable
    'installable': True,
    
    # If True, module appears as an application (has its own menu)
    # If False, it's a technical module (no menu, just functionality)
    'application': True,
}
```

### 💻 Code Example: Top-Level `__init__.py`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\__init__.py`

```python
# This file imports all models so Odoo can find them
# When Odoo loads the module, it executes this file
# which triggers the import of all model classes

from . import models
```

**Explanation:**
- The `.` means "current directory"
- `import models` imports the `models` package (the `models/__init__.py` file)
- This is a relative import - it looks for the `models` folder in the same directory

### 💻 Code Example: `models/__init__.py`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\models\__init__.py`

```python
# Import all model classes from their respective files
# This makes them available to Odoo's ORM (Object-Relational Mapping)

from . import account
from . import journal_entry
```

**Explanation:**
- Each `.py` file in `models/` contains one or more model classes
- We import each file here so Odoo knows about all our models
- When you add a new model file, you must add its import here

---

## 📒 Phase 2: The Chart of Accounts (The Foundation)
We need a model to store "Accounts" (e.g., Bank, Cash, Sales, Expenses).

### 📝 Checklist
- [ ] Create `models/account.py`
- [ ] Define fields: `name`, `code`, `type` (Asset, Liability, etc.)
- [ ] Create a Tree View to see all accounts.
- [ ] Create a Form View for account details.

### 💡 Why Chart of Accounts?

The Chart of Accounts is the foundation of any accounting system. Think of it as a filing system where every financial transaction gets categorized. The "Code" is usually a number (e.g., 1000 for Cash, 2000 for Liabilities) used by accountants to quickly identify accounts. Standard accounting codes follow patterns:
- **1000-1999:** Assets (what you own)
- **2000-2999:** Liabilities (what you owe)
- **3000-3999:** Equity (owner's stake)
- **4000-4999:** Income (money earned)
- **5000-5999:** Expenses (money spent)

### 💻 Complete Code: `models/account.py`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\models\account.py`

```python
# Import Odoo's core components
from odoo import models, fields, api

class ErpAccount(models.Model):
    """
    Chart of Accounts Model
    
    This class represents a single account in the chart of accounts.
    Each account is like a "bucket" where money is tracked.
    
    In Odoo, models inherit from models.Model, which provides:
    - Database table creation
    - CRUD operations (Create, Read, Update, Delete)
    - Search and filtering capabilities
    - Automatic UI generation
    """
    
    # _name: The technical name Odoo uses internally
    # Format: 'module.model' (no spaces, lowercase, dots separate words)
    # This becomes the database table name: 'erp_account'
    _name = 'erp.account'
    
    # _description: Human-readable description shown in UI
    _description = 'Accounting Account'
    
    # _order: Default sorting when records are displayed
    # 'code' means sort by the 'code' field in ascending order
    _order = 'code'

    # ========== FIELD DEFINITIONS ==========
    
    # Char field: Stores text/string data
    # required=True: User MUST fill this field before saving
    # string: Label shown in the UI (can be different from field name)
    name = fields.Char(string='Account Name', required=True)
    
    # Account code (e.g., "1000", "2000")
    # This is what accountants use to quickly identify accounts
    code = fields.Char(string='Code', required=True)
    
    # Selection field: Dropdown with predefined options
    # Format: [('value', 'Label'), ...]
    # 'value' is stored in database, 'Label' is shown to user
    account_type = fields.Selection([
        ('asset', 'Asset'),           # Things you own (Cash, Equipment)
        ('liability', 'Liability'),   # Things you owe (Loans, Payables)
        ('equity', 'Equity'),         # Owner's stake (Capital, Retained Earnings)
        ('income', 'Income'),         # Money earned (Sales, Revenue)
        ('expense', 'Expense')        # Money spent (Rent, Salaries)
    ], string='Type', required=True)
    
    # Computed field: Value is calculated, not directly entered
    # compute='_compute_balance': Method that calculates the value
    # store=True: Store calculated value in database (for performance)
    # Without store=True, it recalculates every time (slower but always current)
    balance = fields.Float(string='Current Balance', compute='_compute_balance', store=True)

    # ========== RELATIONSHIP FIELDS ==========
    
    # One2many: One account has many journal items
    # Format: One2many('related_model', 'foreign_key_field', 'label')
    # 'erp.journal.item': The related model
    # 'account_id': The field in erp.journal.item that points back to this account
    # This creates a reverse relationship - you can access all items for an account
    item_ids = fields.One2many('erp.journal.item', 'account_id', string='Journal Items')

    # ========== COMPUTED METHODS ==========
    
    # @api.depends: Decorator that tells Odoo when to recalculate
    # If 'item_ids.debit' or 'item_ids.credit' changes, recalculate balance
    # This ensures balance is always up-to-date when journal items change
    @api.depends('item_ids.debit', 'item_ids.credit')
    def _compute_balance(self):
        """
        Calculate the current balance of this account.
        
        Balance = Sum of all Debits - Sum of all Credits
        
        Why Debit minus Credit?
        - For Asset/Expense accounts: Debit increases, Credit decreases
        - For Liability/Income/Equity accounts: Credit increases, Debit decreases
        - This formula works for all account types in a simplified way
        
        Note: In a full accounting system, you'd handle account types differently
        """
        # Loop through each record (account) being computed
        # 'self' can be one record or multiple records (when viewing a list)
        for record in self:
            # Get all journal items linked to this account
            items = record.item_ids
            
            # .mapped('debit'): Extract all 'debit' values from items
            # sum(): Add them all together
            total_debits = sum(items.mapped('debit'))
            total_credits = sum(items.mapped('credit'))
            
            # Calculate balance: Debits minus Credits
            # Positive = more debits (money in for assets)
            # Negative = more credits (money out for assets)
            record.balance = total_debits - total_credits
```

### 📚 Understanding Odoo Model Concepts

**1. Model Inheritance (`models.Model`):**
- All Odoo models inherit from `models.Model`
- This provides database persistence, ORM features, and UI integration
- Odoo automatically creates a database table based on your model

**2. Field Types:**
- `Char`: Text fields (names, codes, descriptions)
- `Float`: Decimal numbers (amounts, balances)
- `Selection`: Dropdown with predefined options
- `One2many`: One record has many related records (Account → Journal Items)
- `Many2one`: Many records point to one record (Journal Item → Account)

**3. Computed Fields:**
- Fields that calculate their value from other fields
- Use `@api.depends()` to specify which fields trigger recalculation
- `store=True` caches the value in database (faster but may be stale)
- `store=False` calculates on-the-fly (slower but always current)

**4. Relationship Fields:**
- `One2many`: "One account has many items" - stored on the "many" side
- `Many2one`: "Many items belong to one account" - stored on the "many" side
- These create bidirectional relationships automatically

---

## 🖊️ Phase 3: Journal Entries & Items (The Transactions)
This is where the magic happens. A "Journal Entry" is the header, and "Journal Items" are the lines.

### 📝 Checklist
- [ ] Create `models/journal_entry.py`
- [ ] Define `erp.journal.entry` (The Header: Date, Reference)
- [ ] Define `erp.journal.item` (The Lines: Account, Debit, Credit)
- [ ] **Constraint:** Ensure Total Debit = Total Credit before posting.
- [ ] Add a "Post" button to lock the entry.

### 💡 Understanding Journal Entries

**What is a Journal Entry?**
A Journal Entry is a record of a business transaction. It consists of:
- **Header (Journal Entry):** Contains metadata like date, reference number, status
- **Lines (Journal Items):** Contains the actual debit/credit details

**Real-World Example:**
You sell a product for $500 cash:
- **Journal Entry:** "Sale of Product XYZ - Jan 15, 2026"
- **Line 1:** Debit Cash $500, Credit Sales $500
- **Line 2:** (Optional) Debit Cost of Goods Sold, Credit Inventory

**Why Two Models?**
- **Separation of Concerns:** Header stores transaction info, lines store accounting details
- **Flexibility:** One entry can have multiple lines (multiple accounts affected)
- **Data Integrity:** Easier to validate that all lines balance

**State Management:**
- **Draft:** Entry can be edited, deleted, modified
- **Posted:** Entry is locked, cannot be changed (audit trail requirement)

### 💻 Complete Code: `models/journal_entry.py`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\models\journal_entry.py`

```python
# Import Odoo core components
from odoo import models, fields, api, _
# Import ValidationError for raising user-friendly error messages
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
    
    # Default order: Most recent entries first
    _order = 'date desc, id desc'

    # ========== BASIC FIELDS ==========
    
    # Reference number (e.g., "JE-001", "INV-2026-001")
    # default='/' means if not provided, use '/' as placeholder
    # In production, you'd auto-generate this with a sequence
    name = fields.Char(string='Reference', required=True, default='/')
    
    # Date of the transaction
    # default=fields.Date.context_today: Uses today's date from user's timezone
    # This is smarter than datetime.today() because it respects user settings
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    
    # State field: Tracks workflow status
    # Selection field with two states
    state = fields.Selection([
        ('draft', 'Draft'),      # Can be edited
        ('posted', 'Posted')     # Locked, cannot be edited
    ], string='Status', default='draft', required=True, readonly=True)
    
    # ========== RELATIONSHIP FIELDS ==========
    
    # One2many: One entry has many lines (items)
    # 'erp.journal.item': The related model
    # 'entry_id': The field in journal.item that points back to this entry
    # string='Entry Lines': Label shown in UI
    line_ids = fields.One2many('erp.journal.item', 'entry_id', string='Entry Lines')

    # ========== BUSINESS LOGIC METHODS ==========
    
    def action_post(self):
        """
        Post the journal entry (lock it from editing).
        
        Before posting, we validate:
        1. Entry must have at least 2 lines (double-entry requirement)
        2. Total debits must equal total credits (balanced entry)
        
        After validation, change state to 'posted' (locked).
        """
        # Loop through records (can be one or multiple if called from list view)
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
                    "Journal entry is not balanced!\n"
                    "Total Debits: %(debits).2f\n"
                    "Total Credits: %(credits).2f\n"
                    "Difference: %(diff).2f\n\n"
                    "Debits and Credits must be equal before posting."
                ) % {
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
                    ) % {'label': line.label or 'Untitled'})
                
                if not has_debit and not has_credit:
                    raise ValidationError(_(
                        "Line '%(label)s' has no debit or credit amount!\n"
                        "Each line must have either a debit or a credit."
                    ) % {'label': line.label or 'Untitled'})
            
            # All validations passed - change state to posted
            # This locks the entry from further editing
            record.state = 'posted'
        
        # Return action to refresh the view
        return True
    
    def action_draft(self):
        """
        Reset entry back to draft state (unlock for editing).
        
        In a production system, you might want to restrict this
        to only certain users or add audit logging.
        """
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
    
    # Order lines by sequence (if you add a sequence field later)
    _order = 'entry_id, id'

    # ========== RELATIONSHIP FIELDS ==========
    
    # Many2one: Many items belong to one entry
    # ondelete='cascade': If entry is deleted, delete all its items
    # This prevents orphaned lines in the database
    entry_id = fields.Many2one(
        'erp.journal.entry', 
        string='Entry', 
        required=True,
        ondelete='cascade',  # Delete items when entry is deleted
        index=True  # Database index for faster searches
    )
    
    # Many2one: Many items can reference the same account
    # required=True: Every line MUST have an account
    # This is fundamental to accounting - you can't have a transaction without an account
    account_id = fields.Many2one(
        'erp.account', 
        string='Account', 
        required=True,
        index=True
    )

    # ========== AMOUNT FIELDS ==========
    
    # Debit amount (money going into the account)
    # For Asset/Expense accounts: Debit increases the balance
    # For Liability/Income/Equity accounts: Debit decreases the balance
    debit = fields.Float(string='Debit', default=0.0)
    
    # Credit amount (money going out of the account)
    # For Asset/Expense accounts: Credit decreases the balance
    # For Liability/Income/Equity accounts: Credit increases the balance
    credit = fields.Float(string='Credit', default=0.0)
    
    # Description/label for this line
    # Helps users understand what this transaction line represents
    label = fields.Char(string='Label', required=True)

    # ========== COMPUTED FIELDS ==========
    
    # Computed field: Shows the account's current balance
    # This is useful when viewing journal items to see account status
    account_balance = fields.Float(
        string='Account Balance', 
        related='account_id.balance',
        readonly=True
    )
    
    # Computed field: Shows account code for quick reference
    account_code = fields.Char(
        string='Account Code',
        related='account_id.code',
        readonly=True
    )

    # ========== CONSTRAINTS ==========
    
    @api.constrains('debit', 'credit')
    def _check_debit_credit(self):
        """
        Constraint: A line cannot have both debit and credit.
        
        This is a database-level validation that runs automatically
        when records are created or updated.
        
        @api.constrains: Decorator that triggers validation
        """
        for record in self:
            # Check if both debit and credit have values
            if record.debit and record.credit:
                raise ValidationError(_(
                    "A journal item cannot have both debit and credit amounts!\n"
                    "Line: %(label)s\n"
                    "Please enter either a debit OR a credit, not both."
                ) % {'label': record.label or 'Untitled'})
            
            # Check if neither has a value
            if not record.debit and not record.credit:
                raise ValidationError(_(
                    "A journal item must have either a debit or credit amount!\n"
                    "Line: %(label)s\n"
                    "Please enter either a debit or a credit amount."
                ) % {'label': record.label or 'Untitled'})
```

### 📚 Key Concepts Explained

**1. State Management:**
- `readonly=True` on state field prevents direct editing
- Only methods like `action_post()` can change the state
- This ensures proper workflow control

**2. Validation Methods:**
- `action_post()`: Business logic validation before posting
- `@api.constrains()`: Database-level validation (runs on save)
- `ValidationError`: User-friendly error messages (translated with `_()`)

**3. Relationship Fields:**
- `One2many` (Entry → Items): One entry has many items
- `Many2one` (Item → Entry): Many items belong to one entry
- `ondelete='cascade'`: Automatic cleanup (delete items when entry deleted)

**4. Computed Fields with `related`:**
- `related='account_id.balance'`: Shows related model's field value
- Automatically updates when the related field changes
- Read-only by default (can't edit through this field)

---

## 🎨 Phase 4: User Interface & Kanban (The Dashboard)
We want to see our accounting status visually.

### 📝 Checklist
- [ ] Create `views/account_menus.xml` (Root menu for Accounting)
- [ ] Create `views/account_views.xml` (List and Form for Accounts)
- [ ] Create `views/journal_views.xml` (Form view with a **Notebook** for lines)
- [ ] Create a **Kanban View** for Journal Entries grouped by `state`.

### 💡 Understanding Odoo Views

**What are Views?**
Views are XML definitions that tell Odoo how to display your data. Odoo supports several view types:

1. **Tree View (List View):** Shows records in a table/list format
2. **Form View:** Shows one record in a detailed form
3. **Kanban View:** Shows records as cards, often grouped by status
4. **Search View:** Defines search filters and fields

**Why Multiple Views?**
- Different views serve different purposes
- Users can switch between views based on their task
- Kanban is great for workflow visualization
- Tree view is great for data entry and bulk operations

**View Inheritance:**
- Views can inherit and modify other views
- Allows customization without changing base views
- Essential for extending standard Odoo modules

### 💻 Complete Code: `views/account_menus.xml`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\views\account_menus.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
    Menu Structure for Accounting Module
    
    This file defines the menu hierarchy that appears in Odoo's main menu bar.
    Menus are organized in a tree structure with parent and child menus.
-->

<odoo>
    <!-- 
        Root Menu: "Accounting"
        This appears in the main menu bar at the top of Odoo
    -->
    <menuitem 
        id="menu_accounting_root"
        name="Accounting"
        sequence="10"
        web_icon="accounting,static/description/icon.png"
    />
    
    <!-- 
        Submenu: "Configuration"
        Parent menu: accounting_root
        Contains setup and configuration options
    -->
    <menuitem 
        id="menu_accounting_config"
        name="Configuration"
        parent="menu_accounting_root"
        sequence="10"
    />
    
    <!-- 
        Menu Item: "Chart of Accounts"
        Opens the list view of accounts
        action: Points to the action defined in account_views.xml
    -->
    <menuitem 
        id="menu_accounting_accounts"
        name="Chart of Accounts"
        parent="menu_accounting_config"
        action="action_erp_account_tree"
        sequence="10"
    />
    
    <!-- 
        Submenu: "Transactions"
        Contains all transaction-related menus
    -->
    <menuitem 
        id="menu_accounting_transactions"
        name="Transactions"
        parent="menu_accounting_root"
        sequence="20"
    />
    
    <!-- 
        Menu Item: "Journal Entries"
        Opens the kanban/list view of journal entries
    -->
    <menuitem 
        id="menu_accounting_journal_entries"
        name="Journal Entries"
        parent="menu_accounting_transactions"
        action="action_erp_journal_entry"
        sequence="10"
    />
</odoo>
```

**XML Structure Explained:**
- `<odoo>`: Root element for all Odoo XML files
- `<menuitem>`: Defines a menu item
  - `id`: Unique identifier (used for references)
  - `name`: Display text shown to users
  - `parent`: ID of parent menu (creates hierarchy)
  - `sequence`: Order of appearance (lower = appears first)
  - `action`: ID of action to execute when clicked

### 💻 Complete Code: `views/account_views.xml`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\views\account_views.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
    Views for Chart of Accounts (erp.account model)
    
    This file defines:
    1. Tree View (List): Shows all accounts in a table
    2. Form View: Shows account details in a form
    3. Action: Defines what happens when menu is clicked
-->

<odoo>
    <!-- 
        ACTION: Defines what view to show when menu is clicked
        Actions are like "commands" that tell Odoo what to display
    -->
    <record id="action_erp_account_tree" model="ir.actions.act_window">
        <field name="name">Chart of Accounts</field>
        <field name="res_model">erp.account</field>
        <field name="view_mode">tree,form</field>
        <field name="context">{}</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create your first account!
            </p>
            <p>
                Accounts are the foundation of your accounting system.
                Each account represents a category where money is tracked.
            </p>
        </field>
    </record>

    <!-- 
        TREE VIEW (List View)
        Shows accounts in a table format with columns
    -->
    <record id="view_erp_account_tree" model="ir.ui.view">
        <field name="name">erp.account.tree</field>
        <field name="model">erp.account</field>
        <field name="arch" type="xml">
            <tree string="Chart of Accounts" decoration-info="account_type == 'asset'">
                <!-- 
                    decoration-info: CSS class for styling
                    Makes asset accounts appear with info color (blue)
                -->
                <field name="code"/>
                <field name="name"/>
                <field name="account_type"/>
                <field name="balance" sum="Total Balance"/>
                <!-- 
                    sum="Total Balance": Shows sum at bottom of column
                    Useful for financial totals
                -->
            </tree>
        </field>
    </record>

    <!-- 
        FORM VIEW
        Shows account details in a detailed form
    -->
    <record id="view_erp_account_form" model="ir.ui.view">
        <field name="name">erp.account.form</field>
        <field name="model">erp.account</field>
        <field name="arch" type="xml">
            <form string="Account">
                <!-- Header: Shows at top of form -->
                <header>
                    <!-- Buttons can be added here for actions -->
                </header>
                
                <!-- Sheet: Main content area -->
                <sheet>
                    <!-- Group: Organizes fields into sections -->
                    <group>
                        <group>
                            <field name="code"/>
                            <field name="name"/>
                            <field name="account_type"/>
                        </group>
                        <group>
                            <field name="balance" readonly="1"/>
                            <!-- 
                                readonly="1": Field cannot be edited
                                Balance is computed, so it's read-only
                            -->
                        </group>
                    </group>
                    
                    <!-- Notebook: Tabbed interface -->
                    <notebook>
                        <page string="Journal Items" name="items">
                            <!-- 
                                One2many field: Shows related journal items
                                Creates an inline list view within the form
                            -->
                            <field name="item_ids" nolabel="1">
                                <tree>
                                    <field name="entry_id"/>
                                    <field name="date" readonly="1"/>
                                    <field name="debit"/>
                                    <field name="credit"/>
                                    <field name="label"/>
                                </tree>
                            </field>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

**View Elements Explained:**
- `<tree>`: List/table view
- `<form>`: Detailed form view
- `<group>`: Groups fields together (side-by-side layout)
- `<notebook>`: Creates tabs
- `<page>`: One tab within a notebook
- `decoration-*`: CSS styling based on conditions
- `sum`: Shows column totals

### 💻 Complete Code: `views/journal_views.xml`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\views\journal_views.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
    Views for Journal Entries (erp.journal.entry model)
    
    This file defines:
    1. Kanban View: Visual workflow board
    2. Tree View: List of entries
    3. Form View: Detailed entry with lines
    4. Action: Menu action definition
-->

<odoo>
    <!-- 
        ACTION: Defines default view when "Journal Entries" menu is clicked
    -->
    <record id="action_erp_journal_entry" model="ir.actions.act_window">
        <field name="name">Journal Entries</field>
        <field name="res_model">erp.journal.entry</field>
        <field name="view_mode">kanban,tree,form</field>
        <!-- 
            view_mode: Order of views available
            kanban: Default view (shown first)
            tree: List view
            form: Detail view
        -->
        <field name="context">{}</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create your first journal entry!
            </p>
            <p>
                Journal entries record all accounting transactions.
                Each entry must have balanced debits and credits.
            </p>
        </field>
    </record>

    <!-- 
        KANBAN VIEW
        Shows entries as cards, grouped by state (Draft/Posted)
    -->
    <record id="view_erp_journal_entry_kanban" model="ir.ui.view">
        <field name="name">erp.journal.entry.kanban</field>
        <field name="model">erp.journal.entry</field>
        <field name="arch" type="xml">
            <kanban default_group_by="state" class="o_kanban_dashboard">
                <!-- 
                    default_group_by="state": Groups cards by state field
                    Creates columns: Draft | Posted
                -->
                <field name="name"/>
                <field name="date"/>
                <field name="state"/>
                <field name="line_ids"/>
                
                <!-- Templates: Define how each card looks -->
                <templates>
                    <t t-name="kanban-box">
                        <!-- 
                            Card container
                            oe_kanban_global_click: Makes entire card clickable
                        -->
                        <div class="oe_kanban_global_click">
                            <!-- Card header -->
                            <div class="oe_kanban_content">
                                <div class="o_kanban_record_top">
                                    <div class="o_kanban_record_headings">
                                        <!-- Reference number -->
                                        <strong class="o_kanban_record_title">
                                            <field name="name"/>
                                        </strong>
                                    </div>
                                </div>
                                
                                <!-- Card body -->
                                <div class="o_kanban_record_body">
                                    <div>Date: <field name="date"/></div>
                                    <div>State: <field name="state" widget="badge" 
                                        decoration-success="state == 'posted'"
                                        decoration-info="state == 'draft'"/>
                                    </div>
                                    <!-- 
                                        widget="badge": Shows as colored badge
                                        decoration-*: Color based on state value
                                    -->
                                </div>
                                
                                <!-- Card footer: Show line count -->
                                <div class="o_kanban_record_bottom">
                                    <div class="oe_kanban_bottom_left">
                                        Lines: <field name="line_ids" widget="statinfo"/>
                                        <!-- 
                                            widget="statinfo": Shows count of related records
                                        -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>

    <!-- 
        TREE VIEW (List View)
        Shows entries in a table
    -->
    <record id="view_erp_journal_entry_tree" model="ir.ui.view">
        <field name="name">erp.journal.entry.tree</field>
        <field name="model">erp.journal.entry</field>
        <field name="arch" type="xml">
            <tree string="Journal Entries" decoration-muted="state == 'posted'">
                <!-- 
                    decoration-muted: Posted entries appear grayed out
                -->
                <field name="name"/>
                <field name="date"/>
                <field name="state" widget="badge"/>
                <field name="line_ids" widget="many2many_tags" 
                    options="{'color_field': 'state'}"/>
            </tree>
        </field>
    </record>

    <!-- 
        FORM VIEW
        Shows entry details with lines in a notebook tab
    -->
    <record id="view_erp_journal_entry_form" model="ir.ui.view">
        <field name="name">erp.journal.entry.form</field>
        <field name="model">erp.journal.entry</field>
        <field name="arch" type="xml">
            <form string="Journal Entry">
                <!-- Header: Action buttons -->
                <header>
                    <button name="action_post" 
                        type="object" 
                        string="Post Entry"
                        class="oe_highlight"
                        attrs="{'invisible': [('state', '=', 'posted')]}"
                        confirm="Are you sure you want to post this entry? It cannot be edited afterwards."/>
                    <!-- 
                        type="object": Calls Python method on model
                        class="oe_highlight": Primary button styling (green)
                        attrs: Conditional visibility (hide if already posted)
                        confirm: Shows confirmation dialog before action
                    -->
                    <button name="action_draft" 
                        type="object" 
                        string="Reset to Draft"
                        attrs="{'invisible': [('state', '=', 'draft')]}"/>
                    <field name="state" widget="statusbar" statusbar_visible="draft,posted"/>
                    <!-- 
                        widget="statusbar": Shows workflow state as progress bar
                        statusbar_visible: Which states to show
                    -->
                </header>
                
                <!-- Sheet: Main content -->
                <sheet>
                    <group>
                        <group>
                            <field name="name"/>
                            <field name="date"/>
                        </group>
                        <group>
                            <field name="state" readonly="1"/>
                        </group>
                    </group>
                    
                    <!-- Notebook: Tabbed interface for lines -->
                    <notebook>
                        <page string="Entry Lines" name="lines">
                            <!-- 
                                One2many field: Shows journal items
                                Creates editable inline list
                            -->
                            <field name="line_ids" nolabel="1">
                                <tree editable="bottom">
                                    <!-- 
                                        editable="bottom": New lines added at bottom
                                        Alternative: "top" adds at top
                                    -->
                                    <field name="account_id" options="{'no_create': True}"/>
                                    <!-- 
                                        options="{'no_create': True}": Prevents creating accounts from here
                                    -->
                                    <field name="label"/>
                                    <field name="debit"/>
                                    <field name="credit"/>
                                    <field name="account_code" readonly="1"/>
                                    <field name="account_balance" readonly="1"/>
                                </tree>
                            </field>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

**Advanced View Features Explained:**

1. **Kanban Grouping:**
   - `default_group_by="state"`: Automatically creates columns
   - Each unique state value becomes a column
   - Cards can be dragged between columns

2. **Widgets:**
   - `widget="badge"`: Colored badge display
   - `widget="statusbar"`: Workflow progress bar
   - `widget="statinfo"`: Shows count of related records

3. **Attributes:**
   - `attrs`: Conditional visibility/readonly/required
   - `decoration-*`: CSS styling based on field values
   - `options`: Field-specific configuration

4. **One2many Inline Editing:**
   - `editable="bottom"`: Allows inline editing
   - Users can add/edit lines directly in the form
   - No need to open separate forms for each line

---

## 🔐 Phase 5: Security & Permissions
Accounting data is sensitive. We must define who can see it.

### 📝 Checklist
- [ ] Add `security/ir.model.access.csv`
- [ ] Define read/write/create/unlink permissions for all models.

### 💡 Understanding Odoo Security

**Why Security is Critical:**
- Without security rules, models are invisible to users
- Even if you create perfect models and views, users can't access them
- Security rules define: Who can see what, and what they can do with it

**Security Layers in Odoo:**

1. **Access Rights (ir.model.access):**
   - Defines basic CRUD permissions (Create, Read, Update, Delete)
   - Applied at the model level
   - User must belong to a group with access rights

2. **Record Rules (ir.rule):**
   - More granular control
   - Can restrict access to specific records
   - Example: "Users can only see their own journal entries"

3. **Menu Visibility:**
   - Menus can be hidden from users without access
   - Controlled by group membership

**Security Groups:**
- `base.group_user`: All logged-in users (standard users)
- `base.group_system`: Administrators
- Custom groups can be created for specific roles

### 💻 Complete Code: `security/ir.model.access.csv`

**File Location:** `c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules\accounting\security\ir.model.access.csv`

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_erp_account,erp.account,model_erp_account,base.group_user,1,1,1,1
access_erp_journal_entry,erp.journal.entry,model_erp_journal_entry,base.group_user,1,1,1,1
access_erp_journal_item,erp.journal.item,model_erp_journal_item,base.group_user,1,1,1,1
```

**CSV Column Explanation:**

1. **id:** Unique identifier for this access rule
   - Format: `access_<model_name>`
   - Must be unique across all modules

2. **name:** Human-readable name (usually same as id)

3. **model_id:id:** Technical name of the model
   - Format: `model_<model_name>` (replace dots with underscores)
   - `erp.account` → `model_erp_account`
   - `erp.journal.entry` → `model_erp_journal_entry`

4. **group_id:id:** Security group that gets these permissions
   - `base.group_user`: All standard users
   - `base.group_system`: Administrators only
   - Can reference custom groups you create

5. **perm_read (0 or 1):** Can view records
   - `1` = Yes, `0` = No
   - Without this, users can't even see the model exists

6. **perm_write (0 or 1):** Can edit existing records
   - `1` = Yes, `0` = No
   - Requires `perm_read = 1` to be useful

7. **perm_create (0 or 1):** Can create new records
   - `1` = Yes, `0` = No
   - Without this, users can only view existing data

8. **perm_unlink (0 or 1):** Can delete records
   - `1` = Yes, `0` = No
   - Most restrictive permission (use carefully)

**Example: More Restrictive Security**

For a production system, you might want different permissions:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
# Accountants: Full access
access_erp_account_accountant,erp.account,model_erp_account,accounting.group_accountant,1,1,1,1
access_erp_journal_entry_accountant,erp.journal.entry,model_erp_journal_entry,accounting.group_accountant,1,1,1,1
access_erp_journal_item_accountant,erp.journal.item,model_erp_journal_item,accounting.group_accountant,1,1,1,1

# Regular users: Read-only
access_erp_account_user,erp.account,model_erp_account,base.group_user,1,0,0,0
access_erp_journal_entry_user,erp.journal.entry,model_erp_journal_entry,base.group_user,1,0,0,0
access_erp_journal_item_user,erp.journal.item,model_erp_journal_item,base.group_user,1,0,0,0
```

**Important Notes:**
- CSV files must use comma (`,`) as delimiter
- No spaces after commas
- First line is header (column names)
- Each model needs at least one access rule
- Without access rules, the model is completely invisible to users
- After modifying security, you must upgrade the module for changes to take effect

---

## 🚀 Learning Path: Step-by-Step Execution

This section provides a detailed, educational walkthrough of implementing the accounting module from scratch.

### Step 1: Initialize the Folder Structure

**What You're Doing:** Creating the directory structure that Odoo expects.

**Why This Matters:** Odoo has a specific folder structure convention. Without it, Odoo won't recognize your module.

**Commands to Run (Windows PowerShell):**

```powershell
# Navigate to your addons directory
cd c:\Users\JOSHUA\Documents\odoo18\server\custom_addons\erp-system\src\modules

# Create main module directory
New-Item -ItemType Directory -Path "accounting" -Force

# Create subdirectories
New-Item -ItemType Directory -Path "accounting\models" -Force
New-Item -ItemType Directory -Path "accounting\views" -Force
New-Item -ItemType Directory -Path "accounting\security" -Force
```

**What Gets Created:**
```
accounting/
├── models/
├── views/
└── security/
```

**Next:** Create the `__init__.py` and `__manifest__.py` files (see Phase 1 code examples above).

---

### Step 2: Define the Models (Database Tables)

**What You're Doing:** Creating Python classes that define database tables.

**Why This Matters:** Models are the foundation. They define:
- What data you can store
- How data relates to other data
- What calculations happen automatically

**Files to Create:**
1. `models/__init__.py` - Imports all models
2. `models/account.py` - Chart of Accounts model
3. `models/journal_entry.py` - Journal Entry and Item models

**Key Concepts:**
- Each model class becomes a database table
- Fields become table columns
- Relationships (One2many, Many2one) create foreign keys
- Computed fields don't create columns (unless `store=True`)

**How Odoo Uses Models:**
1. On module install, Odoo reads your model classes
2. Creates corresponding database tables
3. Adds columns for each field
4. Creates indexes for relationship fields
5. Sets up ORM (Object-Relational Mapping) for database access

**Testing Your Models:**
- Install/upgrade the module in Odoo
- Check database: Tables should be created
- Check logs: No errors should appear

---

### Step 3: Define the Security (Access Control)

**What You're Doing:** Creating CSV file that defines who can access your models.

**Why This Matters:** Without security rules:
- Models exist in database but are invisible
- Users can't see menus
- Views won't load
- You'll get "Access Denied" errors

**File to Create:**
- `security/ir.model.access.csv`

**Key Concepts:**
- Each model needs at least one access rule
- Rules are tied to security groups
- Users must belong to a group with access
- Permissions are: Read, Write, Create, Delete

**Testing Security:**
- Install/upgrade module
- Log in as a user
- Check if menus appear
- Try creating/editing records
- Verify permissions work as expected

**Common Mistakes:**
- Forgetting to add model to `__manifest__.py` data files
- Wrong model name format (must be `model_<name>`)
- Not upgrading module after security changes

---

### Step 4: Build the Views (User Interface)

**What You're Doing:** Creating XML files that define how data is displayed.

**Why This Matters:** Views are what users interact with. They define:
- What fields are shown
- How data is organized
- What buttons are available
- How records are filtered and searched

**Files to Create:**
1. `views/account_menus.xml` - Menu structure
2. `views/account_views.xml` - Account list/form views
3. `views/journal_views.xml` - Journal entry views (kanban, tree, form)

**Key Concepts:**
- **Actions:** Define what happens when menu is clicked
- **Views:** Define how data is displayed
- **Widgets:** Special display formats (badges, status bars, etc.)
- **Attributes:** Conditional behavior (visibility, readonly, etc.)

**View Types Explained:**

1. **Tree View (List):**
   - Shows multiple records in a table
   - Good for: Browsing, searching, bulk operations
   - Example: List of all accounts

2. **Form View:**
   - Shows one record in detail
   - Good for: Creating, editing, viewing details
   - Example: Account details with related journal items

3. **Kanban View:**
   - Shows records as cards
   - Good for: Workflow visualization, status tracking
   - Example: Journal entries grouped by Draft/Posted

**Testing Views:**
- Install/upgrade module
- Click menu items
- Verify views load correctly
- Test creating/editing records
- Check that buttons work
- Verify computed fields display correctly

---

### Step 5: Add Business Logic (Python Methods)

**What You're Doing:** Writing Python methods that implement accounting rules.

**Why This Matters:** Business logic ensures:
- Data integrity (balanced entries)
- Workflow control (draft → posted)
- Automatic calculations (account balances)
- Validation (prevent invalid data)

**Methods to Implement:**

1. **`_compute_balance()`** (in `account.py`):
   - Calculates account balance from journal items
   - Runs automatically when items change
   - Updates balance field

2. **`action_post()`** (in `journal_entry.py`):
   - Validates entry is balanced
   - Changes state to 'posted'
   - Locks entry from editing

3. **`_check_debit_credit()`** (in `journal_entry.py`):
   - Validates each line has debit OR credit (not both, not neither)
   - Runs automatically on save

**Key Concepts:**
- **Decorators:** `@api.depends()`, `@api.constrains()`
- **Validation:** `ValidationError` for user-friendly errors
- **State Management:** Controlling workflow transitions
- **Computed Fields:** Automatic calculations

**Testing Business Logic:**
- Create unbalanced entry → Should show error
- Create balanced entry → Should post successfully
- Try to edit posted entry → Should be locked
- Add journal item → Balance should update automatically

---

## ✅ Master Accounting Checklist

### Infrastructure Setup
- [ ] **Folder Structure**
    - [ ] Created `accounting/` directory
    - [ ] Created `accounting/models/` directory
    - [ ] Created `accounting/views/` directory
    - [ ] Created `accounting/security/` directory
    - [ ] Verified all paths match plan

- [ ] **Manifest File**
    - [ ] Created `__manifest__.py` with correct structure
    - [ ] Defined module name, version, description
    - [ ] Added dependencies: `['base']`
    - [ ] Added data files in correct order:
        - [ ] `security/ir.model.access.csv`
        - [ ] `views/account_menus.xml`
        - [ ] `views/account_views.xml`
        - [ ] `views/journal_views.xml`
    - [ ] Set `installable = True`
    - [ ] Set `application = True`

- [ ] **Init Files**
    - [ ] Created top-level `__init__.py` (imports models)
    - [ ] Created `models/__init__.py` (imports account, journal_entry)

### Models (Database Tables)
- [ ] **`erp.account` Model** (`models/account.py`)
    - [ ] Defined `_name = 'erp.account'`
    - [ ] Added field: `name` (Char, required)
    - [ ] Added field: `code` (Char, required)
    - [ ] Added field: `account_type` (Selection with 5 types)
    - [ ] Added field: `balance` (Float, computed, stored)
    - [ ] Added field: `item_ids` (One2many to journal.items)
    - [ ] Implemented `_compute_balance()` method
    - [ ] Added `@api.depends('item_ids.debit', 'item_ids.credit')`
    - [ ] Tested: Balance calculates correctly

- [ ] **`erp.journal.entry` Model** (`models/journal_entry.py`)
    - [ ] Defined `_name = 'erp.journal.entry'`
    - [ ] Added field: `name` (Char, required, default='/')
    - [ ] Added field: `date` (Date, default=today)
    - [ ] Added field: `state` (Selection: draft/posted, readonly)
    - [ ] Added field: `line_ids` (One2many to journal.items)
    - [ ] Implemented `action_post()` method
    - [ ] Added validation: At least 2 lines required
    - [ ] Added validation: Debits must equal credits
    - [ ] Added validation: Each line has debit OR credit
    - [ ] Implemented `action_draft()` method
    - [ ] Tested: Posting works, validation works

- [ ] **`erp.journal.item` Model** (`models/journal_entry.py`)
    - [ ] Defined `_name = 'erp.journal.item'`
    - [ ] Added field: `entry_id` (Many2one, required, cascade delete)
    - [ ] Added field: `account_id` (Many2one, required)
    - [ ] Added field: `debit` (Float, default=0.0)
    - [ ] Added field: `credit` (Float, default=0.0)
    - [ ] Added field: `label` (Char, required)
    - [ ] Added field: `account_balance` (Float, related, readonly)
    - [ ] Added field: `account_code` (Char, related, readonly)
    - [ ] Implemented `@api.constrains('debit', 'credit')`
    - [ ] Tested: Constraints prevent invalid data

### Views (User Interface)
- [ ] **Menu Structure** (`views/account_menus.xml`)
    - [ ] Created root menu: "Accounting"
    - [ ] Created submenu: "Configuration"
    - [ ] Created menu item: "Chart of Accounts" (links to account action)
    - [ ] Created submenu: "Transactions"
    - [ ] Created menu item: "Journal Entries" (links to journal action)
    - [ ] Tested: All menus appear in Odoo

- [ ] **Account Views** (`views/account_views.xml`)
    - [ ] Created action: `action_erp_account_tree`
    - [ ] Created tree view: Shows code, name, type, balance
    - [ ] Added balance sum at bottom of tree
    - [ ] Created form view: Shows account details
    - [ ] Added notebook with "Journal Items" tab
    - [ ] Added One2many field showing related items
    - [ ] Tested: Can view, create, edit accounts

- [ ] **Journal Entry Views** (`views/journal_views.xml`)
    - [ ] Created action: `action_erp_journal_entry`
    - [ ] Created kanban view: Grouped by state
    - [ ] Kanban shows: name, date, state badge, line count
    - [ ] Created tree view: Shows name, date, state
    - [ ] Created form view: Shows entry details
    - [ ] Added "Post Entry" button (hidden when posted)
    - [ ] Added "Reset to Draft" button (hidden when draft)
    - [ ] Added statusbar widget for state
    - [ ] Added notebook with "Entry Lines" tab
    - [ ] Added editable One2many field for lines
    - [ ] Tested: All views work, buttons function correctly

### Security (Access Control)
- [ ] **Access Rules** (`security/ir.model.access.csv`)
    - [ ] Created rule for `erp.account` (read, write, create, delete)
    - [ ] Created rule for `erp.journal.entry` (read, write, create, delete)
    - [ ] Created rule for `erp.journal.item` (read, write, create, delete)
    - [ ] All rules assigned to `base.group_user`
    - [ ] Verified CSV format is correct (commas, no spaces)
    - [ ] Tested: Users can access all models

### Business Logic Testing
- [ ] **Account Balance Calculation**
    - [ ] Created account
    - [ ] Created journal entry with items affecting account
    - [ ] Verified balance updates automatically
    - [ ] Added more items, verified balance recalculates

- [ ] **Journal Entry Validation**
    - [ ] Tried to post entry with 1 line → Error shown ✓
    - [ ] Tried to post unbalanced entry → Error shown ✓
    - [ ] Tried to post entry with line having both debit/credit → Error shown ✓
    - [ ] Posted balanced entry → Success ✓
    - [ ] Tried to edit posted entry → Locked ✓

- [ ] **Journal Item Constraints**
    - [ ] Tried to create item with both debit and credit → Error ✓
    - [ ] Tried to create item with neither debit nor credit → Error ✓
    - [ ] Created valid item → Success ✓

### Final Verification
- [ ] Module installs without errors
- [ ] All menus appear correctly
- [ ] Can create accounts
- [ ] Can create journal entries
- [ ] Can add journal items to entries
- [ ] Can post entries
- [ ] Posted entries are locked
- [ ] Account balances calculate correctly
- [ ] All validations work
- [ ] No errors in Odoo logs

---

## 🎓 Next Steps: Expanding Your Knowledge

Once you've completed the basic accounting module, consider learning:

1. **Advanced Odoo Features:**
   - Record Rules (row-level security)
   - Computed Fields with `store=True` vs `store=False`
   - Model Inheritance (extending existing models)
   - Transient Models (wizards)

2. **Accounting Enhancements:**
   - Account hierarchies (parent/child accounts)
   - Account reconciliation
   - Financial reports (Trial Balance, P&L, Balance Sheet)
   - Multi-currency support
   - Fiscal periods

3. **Odoo Best Practices:**
   - Module structure and organization
   - Naming conventions
   - Error handling
   - Logging and debugging
   - Testing (unit tests, integration tests)

---

**Ready to Start?** Begin with Step 1: Creating the folder structure, then proceed through each phase systematically. Take your time to understand each concept before moving to the next!
