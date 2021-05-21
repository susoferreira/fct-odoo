#-*- coding: utf-8 -*-

from odoo import models, fields, api


class informe(models.Model):
    _name = "informes.informe"
    _description = "Informe"

    fecha = fields.Date()
    instalacion = fields.Char() # nombre de la instalación
    epR = fields.Float()
    emR = fields.Float()
    epS = fields.Float()
    emS = fields.Float()
    epT = fields.Float()
    emT = fields.Float()

    epRST = fields.Float()
    emRST = fields.Float()
    
    Q1 = fields.Float()
    Q2 = fields.Float()
    Q3 = fields.Float()
    Q4 = fields.Float()

    EcR = fields.Float()
    EcS = fields.Float()
    EcT = fields.Float()
    EcRST = fields.Float()
    Einv_tot = fields.Float()
    
    inversor_1 = fields.Float(required=False)
    inversor_2 = fields.Float(required=False)
    inversor_3 = fields.Float(required=False)
    inversor_4 = fields.Float(required=False)
    inversor_5 = fields.Float(required=False)
    propietario = fields.Many2one('res.users','Propietario', default=lambda self: self.env.uid) 
    # el propietario es el usuario que crea los datos