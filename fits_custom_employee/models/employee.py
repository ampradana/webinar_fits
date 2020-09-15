# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    nik = fields.Char(string="NIK")
    tgl_masuk = fields.Date(string="Tgl Masuk")
    agama = fields.Selection([('1','Islam'),('2','Kristen'),('3','Katolik'), ('4','Hindu'), 
                              ('5','Budha')], string="Agama")
    workplace_id = fields.Many2one("hr.workplace", string="Workplace")
    
class HrWorkplace(models.Model):
    _name = 'hr.workplace'
    
    name = fields.Char (string="Nama")
    note = fields.Char (string="Keterangan")
    


