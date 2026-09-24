{
    'name': 'Employee Management',
    'version': '1.0',
    'summary': 'Manage basic employee information',
    'description': 'A simple module for learning Odoo development, managing employees and departments.',
    'category': 'Human Resources',
    'author': 'Satyam',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/department_views.xml',
        'views/employee_views.xml',
    ],
    'installable': True,
    'application': True,
}