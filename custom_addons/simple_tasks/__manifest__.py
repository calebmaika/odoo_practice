{
    "name": "Simple Task",
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
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'views/task_views.xml'
    ],
    "assets": {},
    "installable": True,
    "application": False,
    "auto_install": False,
}