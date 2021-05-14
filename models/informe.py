#-*- coding: utf-8 -*-

from odoo import models, fields, api


class informe(models.Model):
    _name = "informes.informe"
    _description = "Informe"
    name = fields.Char()
    fecha = fields.Date()

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
    Einv_INVERSOR_1 = fields.Float()
