from odoo import models,fields,api

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char('Name')
    age = fields.Integer('Age')

    def action_create(self):
        self.env['student.student'].create({
            'name' : 'Ko Ko',
            'age'  : 25,
        })

    def action_search(self):
        student = self.env['student.student'].search([('name','=','Ko Ko')])
        for rec in student:
            print(rec.name,rec.age)