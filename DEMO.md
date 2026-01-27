# 🎓 Learning Odoo: A Beginner's Guide
## Build Your First Module - "Simple Task Manager"

Welcome! This guide will teach you Odoo like you're learning something new. We'll build a real project step-by-step. Think of Odoo as a **giant toolbox** for running businesses - and you're going to build one tool inside it!

---

## 📚 What is Odoo? (The Simple Version)

Imagine a LEGO set. Odoo is like that set:
- **Odoo Core** = The basic LEGO bricks
- **Modules** = Buildings you create with those bricks
- **Your Task** = Building a small house (a Task Manager module)

Every module you create can talk to other modules and do amazing things! 🏗️

---

## 🎯 Our Project: "Simple Task Manager"

We'll create a module called `simple_tasks` that lets users:
- ✅ Create tasks (like a to-do list)
- ✅ Mark tasks as done or not done
- ✅ Assign tasks to people
- ✅ See all tasks in a list

---

## 🚀 Learning Path - The Checklist

### **Phase 1: Understanding the Basics**
Learn what Odoo needs before we build anything.

- [ ] **Understand Module Structure**
  - A module is a folder with special files inside
  - Think of it like a gift box with instructions
  - Every module needs a "birth certificate" (`__manifest__.py`)
  
- [ ] **Learn About Models**
  - Models are like blueprints for your data
  - Example: A Task model describes what a task looks like
  - Fields: `name`, `description`, `is_done`, `assigned_to`
  
- [ ] **Understand Views**
  - Views are how users SEE your data (like a window)
  - List View: Shows all tasks like a table
  - Form View: Shows one task with all details
  - Search View: Helps find specific tasks

- [ ] **Learn About the Database**
  - Odoo stores data like drawers in a filing cabinet
  - One drawer = One model = One table
  - Each item in that drawer = One record

---

### **Phase 2: Setup (The Foundation)**

Get your tools ready!

- [/] **Create the Module Folder**
  - Location: `custom_addons/simple_tasks/`
  - This is where all your code lives
  
- [/] **Create the `__init__.py` file**
  - Purpose: Tells Odoo "this is a Python package"
  - Location: `custom_addons/simple_tasks/__init__.py`
  
  **Code to add:**
  ```python
  # This file tells Odoo this folder is a module
  from . import models
  ```
  
- [/] **Create the `__manifest__.py` file**
  - Purpose: The "birth certificate" of your module
  - Location: `custom_addons/simple_tasks/__manifest__.py`
  - Contains: Name, version, dependencies, description
  - Odoo reads this to understand your module
  
  **Code to add:**
  ```python
    {
        "name": "Task Management",
        "version": "18.0.1.0.0",
        "category": "Custom",
        "summary": "Sample module for Odoo 18",
        "description": """
            This module helps you manage tasks.
            =====================
            Features:
            - CRUD tasks
            - Mark tasks as done
            - Assign tasks to users
            """,
        "author": "Caleb",
        "website": "https.//www.Caleb.com",
        "license": "LGPL-3",
        "depends": [],
        "data": [],
        "assets": {},
        "installable": True,
        "application": False,
        "auto_install": False,
    }
  ```
  
- [/] **Create the `models/` folder**
  - Purpose: This is where your blueprints (models) go
  - Location: `custom_addons/simple_tasks/models/`
  
- [/] **Create the `views/` folder**
  - Purpose: This is where you design how things look
  - Location: `custom_addons/simple_tasks/views/`
  
- [/] **Create the `security/` folder**
  - Purpose: Who can do what? (Access control)
  - Location: `custom_addons/simple_tasks/security/`

---

### **Phase 3: Build the Model (The Blueprint)**

Create the data structure!

- [ ] **Create `models/__init__.py`**
  - Imports your task model
  - Location: `custom_addons/simple_tasks/models/__init__.py`
  
  **Code to add:**
  ```python
  # This imports the Task model so Odoo can find it
  from . import task
  ```
  
- [/] **Create `models/task.py`**
  - Build the Task model (the blueprint)
  - Location: `custom_addons/simple_tasks/models/task.py`
  - Add fields:
    - `name`: Text (what is the task?)
    - `description`: Text (tell me more)
    - `is_done`: Boolean (yes/no - is it finished?)
    - `priority`: Selection (low/medium/high)
    - `assigned_to`: Relation (who should do it?)
    - `created_date`: Auto (when was it created?)
  
  **Code to add:**
  ```python
  from odoo import models, fields
  
  class SimpleTask(models.Model):
      """
      This is the Task model - the blueprint for tasks.
      Like a recipe card that describes what a task looks like.
      """
      _name = 'simple.task'  # The internal name (database table name)
      _description = 'Simple Task'  # Human-readable name
      
      # FIELDS - Like boxes to fill with information
      name = fields.Char(
          string='Task Name',  # Label shown to users
          required=True,  # Must fill this in
          help='Enter the name of your task'
      )
      
      description = fields.Text(
          string='Description',
          help='Tell me more about this task'
      )
      
      is_done = fields.Boolean(
          string='Done?',
          default=False,  # By default, tasks are NOT done
          help='Check this when the task is finished'
      )
      
      priority = fields.Selection(
          [
              ('low', 'Low Priority'),  # Internal value, Display value
              ('medium', 'Medium Priority'),
              ('high', 'High Priority'),
          ],
          string='Priority',
          default='medium'  # Default to medium priority
      )
      
      assigned_to = fields.Many2one(
          'res.users',  # Connect to Odoo's User model
          string='Assigned To',
          help='Who should do this task?'
      )
      
      created_date = fields.Datetime(
          string='Created On',
          default=fields.Datetime.now  # Auto-filled with current time
      )
      
      # METHODS - Actions you can perform
      def mark_as_done(self):
          """Mark this task as completed"""
          self.is_done = True
      
      def mark_as_not_done(self):
          """Mark this task as not completed"""
          self.is_done = False
      
      def reset_priority(self):
          """Reset priority back to medium"""
          self.priority = 'medium'
  ```

---

### **Phase 4: Create Views (How It Looks)**

Design the user interface!

- [/] **Create `views/task_views.xml`**
  - This is HTML-like code that tells Odoo how to display tasks
  - Location: `custom_addons/simple_tasks/views/task_views.xml`
  
  **Code to add:**
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <odoo>
      <!-- This is the LIST VIEW - shows all tasks like a table -->
      <record id="simple_task_view_tree" model="ir.ui.view">
          <field name="name">Task List</field>
          <field name="model">simple.task</field>
          <field name="arch" type="xml">
              <tree>  <!-- Tree = List view -->
                  <!-- These are the columns that show in the list -->
                  <field name="name" string="Task Name"/>
                  <field name="priority" string="Priority"/>
                  <field name="is_done" string="Done?"/>
                  <field name="assigned_to" string="Assigned To"/>
              </tree>
          </field>
      </record>

      <!-- This is the FORM VIEW - shows one task with all details -->
      <record id="simple_task_view_form" model="ir.ui.view">
          <field name="name">Task Form</field>
          <field name="model">simple.task</field>
          <field name="arch" type="xml">
              <form>  <!-- Form = Detail view -->
                  <sheet>  <!-- This is the main content area -->
                      <h1>
                          <field name="name" placeholder="Enter task name..."/>
                      </h1>
                      
                      <!-- Main fields section -->
                      <group>
                          <group>  <!-- Left column -->
                              <field name="priority" widget="radio"/>
                              <field name="assigned_to"/>
                              <field name="created_date" readonly="True"/>
                          </group>
                          <group>  <!-- Right column -->
                              <field name="is_done" 
                                     label="Mark as Done" 
                                     widget="boolean_toggle"/>
                          </group>
                      </group>
                      
                      <!-- Description section -->
                      <separator string="Description"/>
                      <field name="description" nolabel="1" placeholder="Add more details..."/>
                      
                      <!-- Action buttons -->
                      <footer>
                          <button name="mark_as_done" 
                                  type="object" 
                                  string="Mark Done" 
                                  class="btn-primary"/>
                          <button name="mark_as_not_done" 
                                  type="object" 
                                  string="Mark Pending"/>
                          <button name="reset_priority" 
                                  type="object" 
                                  string="Reset Priority"/>
                      </footer>
                  </sheet>
              </form>
          </field>
      </record>

      <!-- This is the SEARCH VIEW - helps find tasks -->
      <record id="simple_task_view_search" model="ir.ui.view">
          <field name="name">Task Search</field>
          <field name="model">simple.task</field>
          <field name="arch" type="xml">
              <search>  <!-- Search view -->
                  <!-- These fields can be searched -->
                  <field name="name" string="Task Name"/>
                  <field name="assigned_to" string="Assigned To"/>
                  
                  <!-- These are filters that appear as buttons -->
                  <filter name="filter_done" 
                          string="Done Tasks" 
                          domain="[('is_done', '=', True)]"/>
                  <filter name="filter_pending" 
                          string="Pending Tasks" 
                          domain="[('is_done', '=', False)]"/>
                  <filter name="filter_high_priority" 
                          string="High Priority" 
                          domain="[('priority', '=', 'high')]"/>
                  
                  <!-- Grouping options -->
                  <group expand="0" string="Group By">
                      <filter name="group_by_priority" 
                              string="Priority" 
                              context="{'group_by': 'priority'}"/>
                      <filter name="group_by_assigned" 
                              string="Assigned To" 
                              context="{'group_by': 'assigned_to'}"/>
                  </group>
              </search>
          </field>
      </record>

      <!-- MENU ITEM - Add to main menu -->
      <menuitem 
          id="simple_task_menu_root" 
          name="Tasks" 
          sequence="10"/>
      
      <menuitem 
          id="simple_task_menu_items"
          parent="simple_task_menu_root"
          name="My Tasks"
          action="simple_task_action_window"
          sequence="1"/>

      <!-- ACTION - What happens when you click the menu -->
      <record id="simple_task_action_window" model="ir.actions.act_window">
          <field name="name">Tasks</field>
          <field name="res_model">simple.task</field>
          <field name="view_mode">tree,form</field>  <!-- Show list first, then form -->
          <field name="help" type="html">
              <p class="o_view_nocontent_smiling_face">
                  No tasks yet! Create your first task to get started.
              </p>
          </field>
      </record>
  </odoo>
  ```
  
- [/] **Understand the View Components**
  - `<tree>` = List view (multiple records)
  - `<form>` = Detail view (one record)
  - `<search>` = Search and filter options
  - `<field>` = Show a field from your model
  - `<filter>` = Quick filter buttons
  - `<button>` = Action buttons (runs methods)

---

### **Phase 5: Add Security (Who Can Do What?)**

Control access!

- [/] **Create `security/ir_model_access.csv`**
  - Who can: create, read, update, delete (CRUD)
  - Location: `custom_addons/simple_tasks/security/ir_model_access.csv`
  - Groups: Maybe only "Employees" can use tasks
  
  **Code to add (CSV format - like a spreadsheet):**
  ```csv
  id,name,model_id:id,group_id:id,perm_create,perm_read,perm_write,perm_unlink
  access_simple_task_user,Simple Task User,model_simple_task,base.group_user,1,1,1,1
  access_simple_task_manager,Simple Task Manager,model_simple_task,base.group_system,1,1,1,1
  ```
  
  **What does each column mean?**
  - `id`: Unique identifier
  - `name`: Human-readable name
  - `model_id:id`: Which model? (simple.task)
  - `group_id:id`: Which user group? (user = everyone, system = admins)
  - `perm_create`: Can CREATE (1=yes, 0=no)
  - `perm_read`: Can READ (1=yes, 0=no)
  - `perm_write`: Can UPDATE (1=yes, 0=no)
  - `perm_unlink`: Can DELETE (1=yes, 0=no)
  
- [ ] **Add Rules (Optional)**
  - Advanced: Show users only THEIR tasks
  - For now, everyone sees everything
  - Later you can add: `domain="[('assigned_to', '=', uid)]"` to only show assigned tasks

---

### **Phase 6: Update Manifest**

Tell Odoo about everything you created!

- [/] **Update `__manifest__.py`**
  - Add your new files
  - Add menu items
  - Example:
    ```python
    'data': [
        'security/ir_model_access.csv',
        'views/task_views.xml',
    ]
    ```

---

### **Phase 7: Install & Test**

Make it real!

- [/] **Restart Odoo Server**
  - Odoo reads your files
  
- [/] **Go to Apps Menu**
  - Search for "Simple Tasks"
  - Click Install
  
- [/] **Test Your Module**
  - Create a task ✅
  - Edit a task ✅
  - Mark as done ✅
  - Try to find a task ✅
  - Delete a task ✅

---

### **Phase 8: Add the Menu**

Make it easy to find!

- [/] **Create Menu Item**
  - Users click "Simple Tasks" in the menu
  - They see the list of tasks
  
- [/] **Update views XML**
  - Add `<menuitem>` tags
  - Connect to your list view

---

### **Phase 9: Learn Advanced Stuff (Bonus!)**

Go deeper if you want!

- [/] **Add Buttons with Actions**
  - Button: "Mark as Done!" (runs code)
  - Button: "Delete This Task"
  - These are already in your form view!
  
  **Already in the form:**
  ```xml
  <button name="mark_as_done" type="object" string="Mark Done" class="btn-primary"/>
  ```
  
  **Your methods in models/task.py:**
  ```python
  def mark_as_done(self):
      """Mark this task as completed"""
      self.is_done = True
  ```
  
- [/] **Add Relations**
  - "Assigned To" = Link to a person in Odoo
  - Learn how models connect
  
  **Already in your model:**
  ```python
  assigned_to = fields.Many2one(
      'res.users',  # This connects to the User model
      string='Assigned To',
      help='Who should do this task?'
  )
  ```
  
- [/] **Add Calculations (Computed Fields)**
  - "Total Tasks", "Done Count"
  - Using `@api.depends` decorator
  
  **Add this to models/task.py:**
  ```python
  from odoo import models, fields, api
  
  # Add this field to your model:
  task_days_old = fields.Integer(
      string='Days Since Created',
      compute='_compute_days_old',
      help='How many days have passed since this task was created'
  )
  
  # Add this method:
  @api.depends('created_date')
  def _compute_days_old(self):
      """Calculate how many days old this task is"""
      for task in self:
          if task.created_date:
              # Calculate the difference
              today = fields.Datetime.now()
              difference = today - task.created_date
              task.task_days_old = difference.days
          else:
              task.task_days_old = 0
  ```
  
- [/] **Add Filters & Domains**
  - Only show "Pending" tasks
  - Learn how to query data
  
  **Already in your search view:**
  ```xml
  <filter name="filter_done" 
          string="Done Tasks" 
          domain="[('is_done', '=', True)]"/>
  <filter name="filter_pending" 
          string="Pending Tasks" 
          domain="[('is_done', '=', False)]"/>
  ```
  
- [/] **Add Validation (Check Before Saving)**
  
  **Add this to models/task.py:**
  ```python
  from odoo import models, fields, api
  from odoo.exceptions import ValidationError
  
  @api.constrains('priority')
  def _check_priority(self):
      """Make sure priority is valid"""
      valid_priorities = ['low', 'medium', 'high']
      for task in self:
          if task.priority not in valid_priorities:
              raise ValidationError(
                  f"Priority must be one of: {valid_priorities}"
              )
  ```

---

### **Phase 10: Deploy & Share**

Share your creation!

- [ ] **Make sure it works**
  - No errors in the console
  - All features work
  
- [ ] **Write Documentation**
  - What does your module do?
  - How do users use it?
  
- [ ] **Celebrate! 🎉**
  - You built your first Odoo module!

---

## 📖 Key Concepts Explained (Simple Version)

### **Models** 🏗️
Think of a Model like a **recipe card**:
- The card lists all ingredients (fields)
- The recipe (methods) tells you what to do with them
- In Odoo, this is your data structure

**Example:**
```python
from odoo import models, fields

class Task(models.Model):
    _name = 'simple.task'
    
    # FIELDS = Ingredients
    name = fields.Char()
    is_done = fields.Boolean()
    
    # METHODS = Recipe (what to do)
    def mark_as_done(self):
        self.is_done = True
```

### **Views** 👁️
Think of Views like **different windows** to look at the same room:
- List view = Looking through a window seeing everyone in a line
- Form view = Going inside and looking at one person closely
- Search view = Using binoculars to find someone specific

**Example:**
```xml
<tree>  <!-- List view - multiple records -->
    <field name="name"/>
    <field name="is_done"/>
</tree>

<form>  <!-- Form view - single record -->
    <field name="name"/>
    <field name="is_done"/>
    <button name="mark_as_done" type="object" string="Done"/>
</form>
```

### **Fields** 📦
Think of Fields like **boxes to fill**:
- `name`: Box for text (Char)
- `is_done`: Box with Yes/No answer (Boolean)
- `priority`: Box with options (Selection)
- `assigned_to`: Box that links to another model (Many2one)

**Example:**
```python
name = fields.Char(string='Task Name', required=True)
is_done = fields.Boolean(string='Done?', default=False)
priority = fields.Selection([('low', 'Low'), ('high', 'High')])
assigned_to = fields.Many2one('res.users', string='Assigned To')
```

### **XML (Views Code)** 📄
It's like **LEGO instructions**:
- Tags describe what to show
- Attributes describe how to show it
- Fields reference your model data

**Example:**
```xml
<form>
    <field name="name" placeholder="Enter task..."/>
    <field name="is_done" widget="boolean_toggle"/>
    <button name="mark_as_done" type="object" string="Mark Done"/>
</form>
```

### **Python (Models Code)** 🐍
It's like **the brain** of your module:
- Defines data structure (fields)
- Contains logic (methods)
- Handles relationships

**Example:**
```python
class Task(models.Model):
    _name = 'simple.task'
    
    name = fields.Char()
    is_done = fields.Boolean()
    
    def mark_as_done(self):
        """This method changes is_done to True"""
        self.is_done = True
        
    def get_task_status(self):
        """This method returns a status message"""
        if self.is_done:
            return "✅ Done!"
        else:
            return "⏳ Pending"
```

### **CSV (Security)** 🔒
CSV is like **a permission list** (Comma-Separated Values):
- Each row is one permission rule
- Columns are: id, name, model, group, create, read, write, delete

**Example:**
```csv
id,name,model_id:id,group_id:id,perm_create,perm_read,perm_write,perm_unlink
access_task_user,Task User,model_simple_task,base.group_user,1,1,1,1
```
This means: Users can Create, Read, Write, and Delete tasks

---

## � Complete Working Example (All Files)

Here's exactly what each file should contain. Copy these carefully!

### **File 1: `custom_addons/simple_tasks/__init__.py`**
```python
from . import models
```

### **File 2: `custom_addons/simple_tasks/__manifest__.py`**
```python
{
    'name': 'Simple Tasks',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'A simple task manager for learning Odoo',
    'description': """
        This module helps you manage tasks.
        Features:
        - Create tasks
        - Mark tasks as done
        - Assign tasks to people
    """,
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir_model_access.csv',
        'views/task_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
```

### **File 3: `custom_addons/simple_tasks/models/__init__.py`**
```python
from . import task
```

### **File 4: `custom_addons/simple_tasks/models/task.py`**
```python
from odoo import models, fields, api

class SimpleTask(models.Model):
    _name = 'simple.task'
    _description = 'Simple Task'
    
    # TEXT FIELDS
    name = fields.Char(
        string='Task Name',
        required=True,
        help='Enter the name of your task'
    )
    
    description = fields.Text(
        string='Description',
        help='Tell me more about this task'
    )
    
    # BOOLEAN FIELD (Yes/No)
    is_done = fields.Boolean(
        string='Done?',
        default=False,
        help='Check this when the task is finished'
    )
    
    # SELECTION FIELD (Choose from list)
    priority = fields.Selection(
        [
            ('low', 'Low Priority'),
            ('medium', 'Medium Priority'),
            ('high', 'High Priority'),
        ],
        string='Priority',
        default='medium'
    )
    
    # RELATION FIELD (Link to another model)
    assigned_to = fields.Many2one(
        'res.users',
        string='Assigned To',
        help='Who should do this task?'
    )
    
    # AUTO FIELD (Computer fills this)
    created_date = fields.Datetime(
        string='Created On',
        default=fields.Datetime.now
    )
    
    # METHODS (Actions you can do)
    def mark_as_done(self):
        """Mark this task as completed"""
        self.is_done = True
    
    def mark_as_not_done(self):
        """Mark this task as not completed"""
        self.is_done = False
    
    def reset_priority(self):
        """Reset priority back to medium"""
        self.priority = 'medium'
    
    def get_status_message(self):
        """Return a status message"""
        if self.is_done:
            return f"✅ Task '{self.name}' is DONE!"
        else:
            return f"⏳ Task '{self.name}' is PENDING"
```

### **File 5: `custom_addons/simple_tasks/views/task_views.xml`**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- LIST VIEW -->
    <record id="simple_task_view_tree" model="ir.ui.view">
        <field name="name">Task List</field>
        <field name="model">simple.task</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name" string="Task Name"/>
                <field name="priority" string="Priority"/>
                <field name="is_done" string="Done?"/>
                <field name="assigned_to" string="Assigned To"/>
            </tree>
        </field>
    </record>

    <!-- FORM VIEW -->
    <record id="simple_task_view_form" model="ir.ui.view">
        <field name="name">Task Form</field>
        <field name="model">simple.task</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <h1>
                        <field name="name" placeholder="Enter task name..."/>
                    </h1>
                    
                    <group>
                        <group>
                            <field name="priority" widget="radio"/>
                            <field name="assigned_to"/>
                            <field name="created_date" readonly="True"/>
                        </group>
                        <group>
                            <field name="is_done" label="Mark as Done" widget="boolean_toggle"/>
                        </group>
                    </group>
                    
                    <separator string="Description"/>
                    <field name="description" nolabel="1" placeholder="Add more details..."/>
                    
                    <footer>
                        <button name="mark_as_done" type="object" string="Mark Done" class="btn-primary"/>
                        <button name="mark_as_not_done" type="object" string="Mark Pending"/>
                        <button name="reset_priority" type="object" string="Reset Priority"/>
                    </footer>
                </sheet>
            </form>
        </field>
    </record>

    <!-- SEARCH VIEW -->
    <record id="simple_task_view_search" model="ir.ui.view">
        <field name="name">Task Search</field>
        <field name="model">simple.task</field>
        <field name="arch" type="xml">
            <search>
                <field name="name" string="Task Name"/>
                <field name="assigned_to" string="Assigned To"/>
                
                <filter name="filter_done" string="Done Tasks" domain="[('is_done', '=', True)]"/>
                <filter name="filter_pending" string="Pending Tasks" domain="[('is_done', '=', False)]"/>
                <filter name="filter_high_priority" string="High Priority" domain="[('priority', '=', 'high')]"/>
                
                <group expand="0" string="Group By">
                    <filter name="group_by_priority" string="Priority" context="{'group_by': 'priority'}"/>
                    <filter name="group_by_assigned" string="Assigned To" context="{'group_by': 'assigned_to'}"/>
                </group>
            </search>
        </field>
    </record>

    <!-- ACTION -->
    <record id="simple_task_action_window" model="ir.actions.act_window">
        <field name="name">Tasks</field>
        <field name="res_model">simple.task</field>
        <field name="view_mode">tree,form</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                No tasks yet! Create your first task to get started.
            </p>
        </field>
    </record>

    <!-- MENU -->
    <menuitem id="simple_task_menu_root" name="Tasks" sequence="10"/>
    <menuitem id="simple_task_menu_items" parent="simple_task_menu_root" name="My Tasks" action="simple_task_action_window" sequence="1"/>
</odoo>
```

### **File 6: `custom_addons/simple_tasks/security/ir_model_access.csv`**
```csv
id,name,model_id:id,group_id:id,perm_create,perm_read,perm_write,perm_unlink
access_simple_task_user,Simple Task User,model_simple_task,base.group_user,1,1,1,1
access_simple_task_manager,Simple Task Manager,model_simple_task,base.group_system,1,1,1,1
```

---

## 🚀 How to Use This Code

1. **Create the folders** - Make exactly this structure:
   ```
   custom_addons/simple_tasks/
   ├── __init__.py
   ├── __manifest__.py
   ├── models/
   │   ├── __init__.py
   │   └── task.py
   ├── views/
   │   └── task_views.xml
   └── security/
       └── ir_model_access.csv
   ```

2. **Copy the code** - Put the code from each "File" section into the matching file

3. **Restart Odoo** - Shut down and restart the server

4. **Install the module** - Go to Apps → Search "Simple Tasks" → Install

5. **Test it** - Click "Tasks" in the menu and try it out!

---

---

```
custom_addons/
└── simple_tasks/
    ├── __init__.py                 (Import helpers)
    ├── __manifest__.py             (Birth certificate)
    ├── models/
    │   ├── __init__.py
    │   └── task.py                 (The blueprint)
    ├── views/
    │   └── task_views.xml          (How it looks)
    └── security/
        └── ir_model_access.csv     (Who can do what)
```

---

## 💡 Learning Tips

1. **Type Everything Yourself** - Don't copy-paste yet! Typing helps you learn
2. **Make Mistakes** - Errors teach you the most
3. **Read Error Messages** - They tell you what's wrong
4. **Take Breaks** - Your brain needs time to process
5. **Build Small Things First** - Master basics before complex stuff
6. **Ask Questions** - When confused, investigate!

---

## 🔍 Understanding the Code (Line by Line)

### **Understanding Model Code**

```python
from odoo import models, fields, api
# Import: Brings in tools we need from Odoo
```

```python
class SimpleTask(models.Model):
# This says: "Create a new type of data called SimpleTask"
# It inherits from models.Model (which means it's a database table)
```

```python
_name = 'simple.task'
# This is the database name (internal identifier)
# Think of it like the drawer label in a filing cabinet
```

```python
name = fields.Char(string='Task Name', required=True)
# Create a field called 'name'
# Type: Char (short text)
# string: What to show the user
# required=True: User MUST fill this in
```

```python
priority = fields.Selection([('low', 'Low'), ('high', 'High')])
# Create a dropdown field
# User sees: "Low" or "High"
# Behind the scenes: stores 'low' or 'high'
```

```python
assigned_to = fields.Many2one('res.users', string='Assigned To')
# Link to another model (User)
# Many2one: Many tasks can be assigned to ONE user
```

```python
def mark_as_done(self):
    self.is_done = True
# This is a method (action)
# When you click a button, this runs
# self = the current task
# is_done = True means mark it as done
```

### **Understanding View Code**

```xml
<tree>  <!-- This means: LIST VIEW -->
    <field name="name"/>  <!-- Show the name column -->
</tree>
```

```xml
<form>  <!-- This means: DETAIL/FORM VIEW -->
    <field name="name"/>  <!-- Show this field -->
</form>
```

```xml
<button name="mark_as_done" type="object" string="Mark Done"/>
<!-- Button that:
    - Calls the mark_as_done() method
    - Shows text "Mark Done" to users
    - When clicked, runs that method
-->
```

```xml
<field name="priority" widget="radio"/>
<!-- Show priority as RADIO BUTTONS instead of dropdown -->
<!-- widget: Changes how the field looks -->
```

```xml
<filter name="filter_done" string="Done Tasks" domain="[('is_done', '=', True)]"/>
<!-- Filter button that shows only DONE tasks -->
<!-- domain: The rule for filtering
    ('is_done', '=', True) means: "where is_done equals True"
-->
```

### **Understanding CSV Code**

```csv
id,name,model_id:id,group_id:id,perm_create,perm_read,perm_write,perm_unlink
access_simple_task_user,Simple Task User,model_simple_task,base.group_user,1,1,1,1
```

| Column | Meaning | Example |
|--------|---------|---------|
| `id` | Unique identifier | `access_simple_task_user` |
| `name` | Human readable | `Simple Task User` |
| `model_id:id` | Which model? | `model_simple_task` |
| `group_id:id` | Which users? | `base.group_user` (all users) |
| `perm_create` | Can CREATE? | `1` = yes, `0` = no |
| `perm_read` | Can READ? | `1` = yes, `0` = no |
| `perm_write` | Can UPDATE? | `1` = yes, `0` = no |
| `perm_unlink` | Can DELETE? | `1` = yes, `0` = no |

---

## ❓ Common Questions Answered

### **Q: What does `self` mean?**
A: `self` means "the current record". If you're editing a task, `self` = that task.

```python
def mark_as_done(self):
    # self = the task being marked done
    self.is_done = True  # Set THIS task's is_done to True
```

### **Q: What's the difference between `Many2one` and `One2many`?**
A: 
- `Many2one`: Many tasks → ONE person (each task has one owner)
- `One2many`: ONE person → Many tasks (one person can own many tasks)

### **Q: What does `domain="[('is_done', '=', True)]"` mean?**
A: This is a filter rule. It says: "Only show items where is_done is True"

In plain English:
- `is_done` = the field name
- `=` = equals
- `True` = the value

### **Q: Why do files have special names like `__init__.py`?**
A: Names starting with `__` are Python convention for "special files"
- `__init__.py`: Tells Python this folder is a package
- `__manifest__.py`: Tells Odoo about this module

### **Q: What's CSV?**
A: CSV = Comma-Separated Values. It's like an Excel spreadsheet as text.
Each line = one row. Commas = column separators.

### **Q: What does `widget="radio"` do?**
A: It changes HOW the field looks on screen.
- No widget = dropdown
- `widget="radio"` = radio buttons (circles you click)
- `widget="boolean_toggle"` = on/off switch

### **Q: What's `readonly="True"`?**
A: It makes a field READ-ONLY. Users can see it but can't change it.
Good for fields that are auto-filled like created_date.

### **Q: What does `placeholder=` do?**
A: It shows hint text when a field is empty.
Like when you see "Enter your name..." in a form.

---

## 🎯 After You Finish This Project

Once you complete this module, you'll be ready to learn:

1. **Advanced Relations**
   - One2many (one person, many tasks)
   - Many2many (tasks can have multiple people)

2. **Computed Fields**
   - Fields that auto-calculate based on others
   - Example: Total tasks done = count of tasks where is_done=True

3. **Email Integration**
   - Send emails when tasks are created
   - Send reminders for pending tasks

4. **Reports**
   - Generate PDF reports of tasks
   - Create dashboards and charts

5. **Workflow**
   - Change task status automatically
   - Create approval flows

6. **API Integration**
   - Connect to external services
   - Sync data with other systems

---

## 🔗 What You'll Learn

By finishing this project, you'll understand:
- ✅ How Odoo modules are structured
- ✅ How to create data models (blueprints)
- ✅ How to design user interfaces with views
- ✅ How to write basic Python for Odoo
- ✅ How to make your module installable
- ✅ How Odoo stores and retrieves data
- ✅ How security and permissions work
- ✅ The relationship between different parts

---

## 🎬 Next Steps

1. **Start with Phase 1** - Read and understand concepts
2. **Move to Phase 2** - Create your folder structure
3. **Follow each phase** - Don't rush!
4. **Test at Phase 7** - See if everything works
5. **Celebrate at Phase 10** - You did it! 🎉

---

## 📝 Remember

Odoo might seem complicated, but it's really just:
1. **Data** (Models) - What information do you store?
2. **Display** (Views) - How do you show that information?
3. **Logic** (Python) - What actions can you do with that data?
4. **Access** (Security) - Who can use this?

Learn these four things, and you'll understand Odoo! 🚀

---

**Good luck on your journey! You've got this! 💪**
