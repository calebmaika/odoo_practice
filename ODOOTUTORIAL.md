# Odoo 18 Exploration & Learning Tutorial

A comprehensive guide to understand and explore Odoo 18 with practical exercises and a hands-on project.

---

## Table of Contents
1. [Part 1: Understanding Odoo Architecture](#part-1-understanding-odoo-architecture)
2. [Part 2: Setting Up & Running Odoo](#part-2-setting-up--running-odoo)
3. [Part 3: Exploring the Codebase](#part-3-exploring-the-codebase)
4. [Part 4: Working with Modules](#part-4-working-with-modules)
5. [Part 5: Hands-On Project](#part-5-hands-on-project-task-management-system)

---

## Part 1: Understanding Odoo Architecture

### Task 1.1: Learn Odoo Fundamentals
- [ ] Read `README.md` to understand what Odoo is
- [ ] Check `LICENSE` file to understand licensing
- [ ] Review the directory structure at the workspace root
- [ ] Understand that Odoo is built with Python and PostgreSQL
- [ ] Learn that Odoo follows MVC (Model-View-Controller) architecture

**Key Concepts:**
- **Modules**: Self-contained packages that add functionality
- **Models**: Database tables and business logic (in `models.py`)
- **Views**: UI layouts (XML-based: List, Form, Kanban, Graph)
- **Controllers**: Handle HTTP requests (in `http.py`)
- **Fields**: Data types for model attributes

### Task 1.2: Understand the Folder Structure
- [ ] Review `/odoo` folder - contains core Odoo framework
- [ ] Check `/odoo/addons` - built-in modules like `account`, `sale`, `crm`
- [ ] Explore `/custom_addons/test_module` - example custom module
- [ ] Look at `/setup` - installation and deployment scripts
- [ ] Examine root config files: `setup.py`, `requirements.txt`, `odoo.conf`

### Task 1.3: Study Core Files
- [ ] Read `odoo/__init__.py` - initialization
- [ ] Check `odoo/models.py` - base model class definition
- [ ] Review `odoo/fields.py` - field type definitions
- [ ] Understand `odoo/http.py` - web controller framework
- [ ] Look at `odoo/api.py` - decorators and API methods

---

## Part 2: Setting Up & Running Odoo

### Task 2.1: Check Requirements
- [ ] Open `requirements.txt` and understand dependencies
- [ ] Verify Python version (Odoo 18 requires Python 3.10+)
- [ ] Check if PostgreSQL is mentioned (required database)

**Command to run:**
```bash
python --version
```

### Task 2.2: Configure Odoo
- [ ] Review `odoo.conf` - configuration file
- [ ] Understand key settings like `db_host`, `db_port`, `db_name`
- [ ] Note the `addons_path` configuration (tells Odoo where to find modules)

### Task 2.3: Start Odoo Server (Optional Practice)
- [ ] Understand the `odoo-bin` file - main entry point
- [ ] Review startup documentation if available
- [ ] (Optional) Run: `python odoo-bin --help` to see available options

**Key Startup Options:**
```
--database=DB_NAME          # Specify database
--port=PORT                 # Server port (default 8069)
--addons-path=PATH          # Path to addons
--dev=all                   # Development mode with auto-reload
```

---

## Part 3: Exploring the Codebase

### Task 3.1: Navigate Core Modules
- [ ] Explore `odoo/addons/base` - foundation module for all others
- [ ] Check `odoo/addons/account` - accounting features
- [ ] Review `odoo/addons/sale` - sales management
- [ ] Look at `odoo/addons/web` - web interface components

### Task 3.2: Understand Module Structure
Navigate to any module (e.g., `odoo/addons/account`):
- [ ] Find `__manifest__.py` - metadata about the module
- [ ] Locate `models/` - contains model definitions
- [ ] Check `views/` - XML files defining UI layouts
- [ ] Review `controllers/` - web routes and controllers
- [ ] Look for `security/ir.model.access.csv` - access controls
- [ ] Examine `data/` or `demo/` - sample data

### Task 3.3: Analyze a Manifest File
- [ ] Open `custom_addons/test_module/__manifest__.py`
- [ ] Understand fields: `name`, `version`, `depends`, `installable`, `data`
- [ ] Learn what `depends` means (dependencies on other modules)

**Example Manifest Structure:**
```python
{
    'name': 'Module Name',
    'version': '1.0',
    'category': 'Category',
    'depends': ['base'],  # Depends on these modules
    'data': [
        'security/ir.model.access.csv',
        'views/module_views.xml',
    ],
    'installable': True,
}
```

### Task 3.4: Read a Model Definition
- [ ] Find and open any model file in `models/`
- [ ] Understand class structure: `class MyModel(models.Model):`
- [ ] Identify field definitions (char, integer, many2one, one2many, etc.)
- [ ] Look for methods decorated with `@api.model` or `@api.onchange`
- [ ] Study computed fields and constraints

### Task 3.5: Study Views (XML)
- [ ] Find XML view files in any module's `views/` folder
- [ ] Understand different view types:
  - [ ] List view - tabular display
  - [ ] Form view - detailed record display
  - [ ] Search view - filtering and searching
  - [ ] Kanban view - card-based display
- [ ] Understand field attributes in views

---

## Part 4: Working with Modules

### Task 4.1: Create a New Custom Module Structure
- [ ] Navigate to `custom_addons/`
- [ ] Create new folder `my_learning_module`
- [ ] Create these files:
  - [ ] `__init__.py` (empty or with imports)
  - [ ] `__manifest__.py` (module metadata)
  - [ ] `models/__init__.py` 
  - [ ] `models/models.py` (model definitions)
  - [ ] `views/__init__.py`
  - [ ] `views/views.xml` (UI layouts)
  - [ ] `security/ir.model.access.csv` (access controls)

**Directory structure:**
```
my_learning_module/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── models.py
├── views/
│   ├── __init__.py
│   └── views.xml
└── security/
    └── ir.model.access.csv
```

### Task 4.2: Write Your First Model
- [ ] Define a simple model in `models/models.py`
- [ ] Add basic fields (name, description, date, etc.)
- [ ] Include a `_name` attribute
- [ ] Add a `_description` attribute

### Task 4.3: Create Views
- [ ] Write a list view XML
- [ ] Write a form view XML
- [ ] Add search filters
- [ ] Reference your model correctly

### Task 4.4: Set Up Access Controls
- [ ] Create `security/ir.model.access.csv`
- [ ] Define read, write, create, delete permissions

### Task 4.5: Update the Manifest
- [ ] Add correct dependencies
- [ ] List all data files
- [ ] Set `installable=True`

---

## Part 5: Hands-On Project: Task Management System

### Project Overview
Build a simple **Task Management Module** for Odoo 18 where you can:
- Create and manage tasks
- Assign tasks to users
- Set priority levels and due dates
- Track task status
- View tasks in different formats (list, kanban, calendar)

### Project Task Checklist

#### Phase 1: Planning & Setup
- [ ] Create module folder: `custom_addons/task_management`
- [ ] Create all required subdirectories
- [ ] Set up basic module files (`__init__.py`, `__manifest__.py`)

#### Phase 2: Database Models
- [ ] Create `Task` model with fields:
  - [ ] `name` (Char) - Task title
  - [ ] `description` (Text) - Task details
  - [ ] `priority` (Selection: Low, Medium, High)
  - [ ] `status` (Selection: New, In Progress, Done, Cancelled)
  - [ ] `assigned_to` (Many2one -> res.users)
  - [ ] `due_date` (Date)
  - [ ] `created_date` (Datetime, auto-set)
  - [ ] `completion_date` (Datetime, nullable)

- [ ] Create `TaskCategory` model:
  - [ ] `name` (Char) - Category name
  - [ ] `description` (Text)
  - [ ] Add Many2one relationship to Task

#### Phase 3: Views & User Interface
- [ ] Create **List View**:
  - [ ] Display: name, priority, status, assigned_to, due_date
  - [ ] Add colors based on priority/status
  
- [ ] Create **Form View**:
  - [ ] Organize fields in logical groups
  - [ ] Add buttons for status transitions (Mark as Done, Cancel)
  
- [ ] Create **Kanban View**:
  - [ ] Group by status
  - [ ] Display priority with different card colors
  
- [ ] Create **Search View**:
  - [ ] Filter by priority
  - [ ] Filter by assigned user
  - [ ] Filter by status
  - [ ] Filter by due date range

#### Phase 4: Business Logic
- [ ] Add method to mark task as done:
  - [ ] Set status to "Done"
  - [ ] Set completion_date to current time
  
- [ ] Add method to get overdue tasks:
  - [ ] Find tasks with due_date < today and status != "Done"
  
- [ ] Add validation:
  - [ ] Can't mark done without due_date
  - [ ] Can't set past due_date
  
- [ ] Add computed field:
  - [ ] `days_remaining` - calculated from due_date

#### Phase 5: Security & Access Control
- [ ] Create `security/ir.model.access.csv`:
  - [ ] User role - can create/read/write own tasks
  - [ ] Manager role - can manage all tasks
  - [ ] Admin role - full access

#### Phase 6: Sample Data
- [ ] Create `data/task_categories_demo.xml`:
  - [ ] Add 3-5 sample task categories (Work, Personal, Urgent, etc.)
  
- [ ] Create `data/sample_tasks_demo.xml`:
  - [ ] Add 5-10 sample tasks in various statuses

#### Phase 7: Testing & Refinement
- [ ] Test module installation
- [ ] Create a few sample tasks via UI
- [ ] Test filtering and searching
- [ ] Test status transitions
- [ ] Verify access controls work
- [ ] Check views render correctly
- [ ] Test business logic methods

#### Phase 8: Enhancement (Optional)
- [ ] Add task dependencies (task A must be done before B)
- [ ] Add subtasks feature
- [ ] Add estimated hours and actual hours worked
- [ ] Add comments/notes on tasks
- [ ] Create dashboard showing task statistics
- [ ] Add email notifications for due tasks
- [ ] Add task templates

---

## Project File Templates

### Step 1: Create __manifest__.py
```python
{
    'name': 'Task Management',
    'version': '1.0.0',
    'category': 'Productivity',
    'summary': 'Simple task management system',
    'description': 'Manage tasks, priorities, and assignments',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
        'views/category_views.xml',
        'data/task_categories_demo.xml',
        'data/sample_tasks_demo.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
```

### Step 2: Create models/models.py
```python
from odoo import models, fields, api
from datetime import datetime

class TaskCategory(models.Model):
    _name = 'task.category'
    _description = 'Task Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')


class Task(models.Model):
    _name = 'task.task'
    _description = 'Task'

    name = fields.Char(string='Task Title', required=True)
    description = fields.Text(string='Description')
    priority = fields.Selection(
        [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string='Priority',
        default='medium'
    )
    status = fields.Selection(
        [('new', 'New'), ('in_progress', 'In Progress'), 
         ('done', 'Done'), ('cancelled', 'Cancelled')],
        string='Status',
        default='new'
    )
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    due_date = fields.Date(string='Due Date')
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now)
    completion_date = fields.Datetime(string='Completion Date')
    category_id = fields.Many2one('task.category', string='Category')

    @api.onchange('status')
    def _onchange_status(self):
        if self.status == 'done':
            self.completion_date = fields.Datetime.now()

    def action_mark_done(self):
        self.status = 'done'
        self.completion_date = fields.Datetime.now()

    @api.model
    def get_overdue_tasks(self):
        return self.search([
            ('due_date', '<', fields.Date.today()),
            ('status', '!=', 'done')
        ])
```

### Step 3: Create views/task_views.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <!-- List View -->
    <record id="task_list_view" model="ir.ui.view">
        <field name="name">task.task.list</field>
        <field name="model">task.task</field>
        <field name="arch" type="xml">
            <list string="Tasks">
                <field name="name"/>
                <field name="priority"/>
                <field name="status"/>
                <field name="assigned_to"/>
                <field name="due_date"/>
            </list>
        </field>
    </record>

    <!-- Form View -->
    <record id="task_form_view" model="ir.ui.view">
        <field name="name">task.task.form</field>
        <field name="model">task.task</field>
        <field name="arch" type="xml">
            <form string="Task">
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="description"/>
                        <field name="priority"/>
                        <field name="status"/>
                        <field name="assigned_to"/>
                        <field name="due_date"/>
                        <field name="category_id"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <!-- Action to display tasks -->
    <record id="task_action" model="ir.actions.act_window">
        <field name="name">Tasks</field>
        <field name="res_model">task.task</field>
        <field name="view_mode">list,form</field>
        <field name="view_id" ref="task_list_view"/>
    </record>

    <!-- Menu item -->
    <menuitem id="task_menu" name="Tasks" action="task_action" sequence="10"/>
</odoo>
```

---

## Learning Tips

1. **Read Before Writing**: Always examine existing modules before creating new ones
2. **Use the Shell**: Use Odoo's Python shell to experiment with models:
   ```bash
   python odoo-bin shell
   # Then: Task = env['task.task']
   ```
3. **Check Logs**: Odoo logs are helpful; watch the terminal while testing
4. **Incremental Testing**: Test each component as you build it
5. **API Documentation**: Keep Odoo API docs nearby
6. **Follow Patterns**: Copy structure from existing modules
7. **Use Debug Mode**: Start with `--dev=all` flag for auto-reload

---

## Useful Commands

```bash
# View available modules
python odoo-bin -l all

# Update a module after changes
python odoo-bin -u task_management

# Dry run database test
python odoo-bin --test-tags=test_task_management

# Interactive shell
python odoo-bin shell

# See all command options
python odoo-bin --help
```

---

## Next Steps After This Tutorial

1. **Advanced Models**: Learn about inheritance, constraints, and computed fields
2. **Advanced Views**: Master XML view syntax with domains, filters, and decorators
3. **Reports**: Create PDF reports using QWeb
4. **Wizards**: Build multi-step wizards for complex operations
5. **API Integration**: Learn to create REST API endpoints
6. **Testing**: Write automated tests for your models
7. **Performance**: Learn database queries optimization and caching
8. **Security**: Master row-level and field-level access controls

---

## Resources

- Odoo Official Documentation: https://www.odoo.com/documentation/18.0
- Python ORM Methods: Available in `odoo/models.py`
- Field Types: Available in `odoo/fields.py`
- API Decorators: Available in `odoo/api.py`

---

**Good luck with your Odoo learning journey! Start with Part 1, and work through each section systematically.**
