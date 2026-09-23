from odoo import models, fields

class EmployeeDepartment(models.Model):
    _name = 'employee.department'
    _description = 'Employee Department'

    name = fields.Char(string='Department Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    
    # One2many relation linking back to employees
    employee_ids = fields.One2many(
        'employee.management', 
        'department_id', 
        string='Employees'
    )