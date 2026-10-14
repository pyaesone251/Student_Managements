from odoo import models,fields,api

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char('Class Name')