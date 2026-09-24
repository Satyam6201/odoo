{
    'name': 'College Student Management System',
    'version': '1.0',
    'summary': 'Manage college students, departments, and courses',
    'description': 'A simple module to manage student information, departments, and courses in a college.',
    'author': 'Antigravity',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/department_views.xml',
        'views/course_views.xml',
        'views/student_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
