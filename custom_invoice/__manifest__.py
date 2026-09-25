{
    "name": "Custom Invoice (Tally Style)",
    "version": "1.0",
    "depends": ["account"],
    "author": "Your Name",
    "category": "Accounting",
    "description": """
    Custom invoice module that provides a Tally-style PDF report.
    """,
    "data": [
        "views/account_move_views.xml",
        "report/invoice_report.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}