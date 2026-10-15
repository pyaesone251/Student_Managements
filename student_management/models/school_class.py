from odoo import models,fields,api

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char('Class Name')
    student_ids = fields.One2many('school.student','class_id',string='Students')

    def action_count(self):
        self.ensure_one()
        count = len(self.student_ids)

        return{
            'type':'ir.actions.client',
            'tag':'display_notification',
            'params':{
                'title':self.name,
                'message':f'Student Count{count}',
                'type':'info',
                'sicky':False,
            }
        }

    def action_write(self):
        self.ensure_one()
        for stuent in self.student_ids:
            stuent.write({
                'age': stuent.age + 15,
            })

    def action_age(self):
        self.ensure_one()
        for stu in self.student_ids:
            if stu.age < 18:
                stu.write({
                    'age':stu.age +1,
                })

