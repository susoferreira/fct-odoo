
from odoo import models, fields, api


class informe(models.Model):
    _name = "informes.inversor"
    _description = "Inversor"
    name=fields.Char(required=True)
    