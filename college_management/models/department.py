from odoo import models, fields

class Department(models.Model):
    _name = 'college.department'
    _description = 'College Department'

    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Department Code', required=True)
    hod_name = fields.Char(string='HOD Name')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)

    # One Department can have many students
    student_ids = fields.One2many('college.student', 'department_id', string='Students')
    
    # One Department can have many courses
    course_ids = fields.One2many('college.course', 'department_id', string='Courses')