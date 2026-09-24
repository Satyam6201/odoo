from odoo import models, fields

class Student(models.Model):
    _name = 'college.student'
    _description = 'College Student'

    # Personal Information
    name = fields.Char(string='Student Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    profile_image = fields.Image(string='Profile Image')

    # Contact Information
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    city = fields.Char(string='City')

    # Academic Information
    roll_number = fields.Char(string='Roll Number', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    semester = fields.Selection([
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
        ('3', '3rd Semester'),
        ('4', '4th Semester'),
        ('5', '5th Semester'),
        ('6', '6th Semester'),
        ('7', '7th Semester'),
        ('8', '8th Semester'),
    ], string='Semester')
    admission_date = fields.Date(string='Admission Date')
    active = fields.Boolean(string='Active', default=True)

    # Relationships
    # Many Students belong to One Department
    department_id = fields.Many2one('college.department', string='Department')
    
    # Many Students belong to One Course
    course_id = fields.Many2one('college.course', string='Course')
