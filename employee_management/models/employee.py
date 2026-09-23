from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EmployeeManagement(models.Model):
    _name = 'employee.management'
    _description = 'Employee Management'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    adharcard = fields.Char(string='Aadhar Card')
    salary = fields.Float(string='Salary')
    joining_date = fields.Date(string='Joining Date')
    job_position = fields.Char(string='Job Position')
    active = fields.Boolean(string='Active', default=True)
    
    # Many2one relation linking to department
    department_id = fields.Many2one(
        'employee.department', 
        string='Department'
    )

    # Computed field
    annual_salary = fields.Float(
        string='Annual Salary', 
        compute='_compute_annual_salary', 
        store=True
    )

    @api.depends('salary')
    def _compute_annual_salary(self):
        for record in self:
            record.annual_salary = record.salary * 12

    @api.constrains('salary')
    def _check_salary(self):
        for record in self:
            if record.salary < 0:
                raise ValidationError("Employee salary cannot be negative.")

    @api.constrains('joining_date')
    def _check_joining_date(self):
        for record in self:
            if record.joining_date and record.joining_date > fields.Date.today():
                raise ValidationError("Joining date cannot be in the future.")