from odoo import models, fields, api

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Record'

    photo = fields.Image(string='Student Photo', max_width=1024, max_height=1024)
    name = fields.Char(string='Student Name', required=True)
    enrollment_date = fields.Date(string='Date of Enrollment')
    academic_year = fields.Char(string='Academic Year')
    mode_of_study = fields.Selection([
        ('regular', 'Regular'),
        ('distance', 'Distance')
    ], string='Mode of Study')
    course_id = fields.Many2one('product.product', string='Course Applied For',
        domain=[('type', '=', 'service')], required=True)
    branch = fields.Char(string='Branch')
    second_language = fields.Char(string='Second Language')
    batch_no = fields.Char(string='Batch No')
    university = fields.Char(string='University')

    # Communication Address
    comm_flat_no = fields.Char(string='Flat/House No.')
    comm_street = fields.Char(string='Street Name')
    comm_post_office = fields.Char(string='Post Office')
    comm_district = fields.Char(string='District')
    comm_state = fields.Char(string='State')
    comm_pincode = fields.Char(string='Pin Code')

    # Permanent Address
    perm_flat_no = fields.Char(string='Permanent Flat/House No.')
    perm_street = fields.Char(string='Permanent Street Name')
    perm_locality = fields.Char(string='Locality')
    perm_district = fields.Char(string='Permanent District')
    perm_state = fields.Char(string='Permanent State')
    perm_pincode = fields.Char(string='Permanent Pin Code')

    # Contact Details
    phone = fields.Char(string='Phone No.')
    whatsapp = fields.Char(string='Whatsapp No.')
    email = fields.Char(string='E-mail Id')

    # Academic Records
    academic_records_ids = fields.One2many('student.academic.record', 'student_id', string='Academic Records')

    # Parent Details
    father_name = fields.Char(string="Father's Name")
    father_age = fields.Integer(string="Father's Age")
    father_occupation = fields.Char(string="Father's Occupation")
    father_contact = fields.Char(string="Father's Contact No.")
    mother_name = fields.Char(string="Mother's Name")
    mother_age = fields.Integer(string="Mother's Age")
    mother_occupation = fields.Char(string="Mother's Occupation")
    mother_contact = fields.Char(string="Mother's Contact No.")

    # Additional Details
    admission_no = fields.Char(string='Admission No.')
    university_enrollment_no = fields.Char(string='University Enrollment No.')
    student_email = fields.Char(string='Student Email')
    
class StudentAcademicRecord(models.Model):
    _name = 'student.academic.record'
    _description = 'Student Academic Record'

    student_id = fields.Many2one('student.student', string='Student')
    exam_passed = fields.Char(string='Qualifying Exam Passed')
    institution = fields.Char(string='Institution')
    year = fields.Integer(string='Year')
    percentage = fields.Float(string='Percentage')
