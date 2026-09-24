from odoo import models, fields

class Course(models.Model):
    _name = 'college.course'
    _description = 'College Course'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    duration = fields.Integer(string='Duration (in years)')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)

    # Many Courses belong to One Department
    department_id = fields.Many2one('college.department', string='Department')
