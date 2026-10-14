from odoo import models,fields,api
from odoo.exceptions import UserError

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char('Student Name')
    age = fields.Integer('Age')
    class_id = fields.Many2one('school.class',string='Class')

    def action_create(self):
        stu = self.env['school.student'].create({
            'name':'TestKyaw Kyaw',
            'age':16,
        })
        return{
            'type':'ir.actions.act_window',
            'name':'Student Create',
            'res_model':'school.student',
            'view_mode':'form',
            'res.id':stu.id,
            'target':'current',
        }

    def action_search(self):
        students = self.env['school.student'].search([
            ('age','>=',18),('name','ilike','Test')
        ])
        return{
            'type':'ir.actions.act_window',
            'name':'Student Search',
            'res_model':'school.student',
            'view_mode':'list',
            'domain':[('id','in',students.ids)],
            'target':'current',
        }

    def action_write(self):
        self.ensure_one()
        self.write({
            'age': self.age +1,
        })

    def action_all_write(self):
        students = self.env['school.student'].search([
            ('name','ilike','Test')
        ])
        
        for stt in students:
            stt.write({
                'age': stt.age +2
            })

        return{
            'name':'Student Write',
            'type':'ir.actions.act_window',
            'res_model':'school.student',
            'view_mode':'list',
            'domain':[('id','in',students.ids)],
            'target':'current'
        }

    def action_delete(self):
        self.ensure_one()
        self.unlink()
        return{
            'type':'ir.actions.act_window',
            'name':'Student Delete',
            'res_model':'school.student',
            'view_mode':'list'
        }

    def action_show_class(self):
        self.ensure_one()

        message = (
            self.class_id.name
            if self.class_id
            else 'No class selected'
        )

        return{
            'type':'ir.actions.client',
            'tag':'display_notification',
            'params':{
                'title':'Student Class',
                'message':message,
                'type':'info',
                'sticky':False,
            }
        }

    def action_class_move(self):
        self.ensure_one()
        school_class = self.env['school.class'].search([
            ('name','=','Class C'),
        ],limit=1)

        if not school_class:
            raise UserError('Create you are Class B')

        self.write({
            'class_id':school_class.id,
        })

    def action_search_class(self):
        self.ensure_one()

        if not self.class_id:
            raise UserError('User False')

        search_class = self.env['school.student'].search([
            ('class_id','=',self.class_id.id),
        ])

        return{
            'type':'ir.actions.act_window',
            'name':'Student in my class',
            'res_model':'school.student',
            'view_mode':'list',
            'domains' : [('id','in',search_class.ids)],
            'target' : 'current',
        }