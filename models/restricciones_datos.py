#-*- coding: utf-8 -*-

from odoo import models, fields, api


class informe(models.Model):
    _name = "informes.restricciones_datos"
    _description = "Máximos y míninimos de los datos usados para la comprobación de los informes"

    min_epR = fields.Float()
    min_emR = fields.Float()
    min_epS = fields.Float()
    min_emS = fields.Float()
    min_epT = fields.Float()
    min_emT = fields.Float()

    min_epRST = fields.Float()
    min_emRST = fields.Float()
    
    min_Q1 = fields.Float()
    min_Q2 = fields.Float()
    min_Q3 = fields.Float()
    min_Q4 = fields.Float()

    min_EcR = fields.Float()
    min_EcS = fields.Float()
    min_EcT = fields.Float()
    min_EcRST = fields.Float()
    min_Einv_tot = fields.Float()
    
    min_inversor_1 = fields.Float(required=False)
    min_inversor_2 = fields.Float(required=False)

    max_emR = fields.Float()
    max_epR = fields.Float()
    max_epS = fields.Float()
    max_emS = fields.Float()
    max_epT = fields.Float()
    max_emT = fields.Float()

    max_epRST = fields.Float()
    max_emRST = fields.Float()
    
    max_Q1 = fields.Float()
    max_Q2 = fields.Float()
    max_Q3 = fields.Float()
    max_Q4 = fields.Float()

    max_EcR = fields.Float()
    max_EcS = fields.Float()
    max_EcT = fields.Float()
    max_EcRST = fields.Float()
    max_Einv_tot = fields.Float()

    max_inversor_1 = fields.Float(required=False)
    max_inversor_2 = fields.Float(required=False)

    