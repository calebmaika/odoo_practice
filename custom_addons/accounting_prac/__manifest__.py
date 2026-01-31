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
    'author': 'Caleb',
    'webiste': 'https.//www.calebmaika.com',
    'license': 'LGPL-3',
    # List of modules this module depends on
    # 'base' is always required - it provides core Odoo functionality
    'depends': ['base'],
    
    # List of data files to load when module is installed
    # Order matters! Security must load before views that reference it
    'data': [
        'security/ir.model.access.csv',  # Load security rules first      
        'views/account_views.xml',       
        'views/journal_views.xml',   
        'views/account_menus.xml',     
    ],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
}