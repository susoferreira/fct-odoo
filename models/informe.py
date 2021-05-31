#-*- coding: utf-8 -*-

from odoo import models, fields, api


class informe(models.Model):
    _name = "informes.informe"
    _description = "Informe"

    fecha = fields.Date()
    planta = fields.Char()

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

    propietario = fields.Many2one('res.users','Propietario', default=lambda self: self.env.uid) 
    # el propietario es el usuario que crea los datos
    restricciones = fields.Many2one("informes.restricciones_datos") 
    estado = fields.Char(compute='comprobar_valores', store=False) #si se guarda en la base de datos reduce el rendimiento pero es necesario para usarlo en la graph view




    @api.depends("restricciones") #cuando cambien las restricciones se volverá a calcular el módulo
    def comprobar_valores(self):
        """
        comprueba si todos los valores están dentro del rango de las restricciones
        si restricciones.min_x y restricciones.max_x son iguales a 0 en ese campo no se comprobarán las restricciones
        """

        for record in self:
            if not record.restricciones:
                record.estado="correcto"
                continue

            
            if (
                    (record.restricciones.max_epR == 0 and record.restricciones.min_epR ==0 )
                or
                    (record.epR < record.restricciones.max_epR and record.epR > record.restricciones.min_epR)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: epR"
                continue

            if (
                    (record.restricciones.max_emR == 0 and record.restricciones.min_emR ==0 )
                or
                    (record.emR < record.restricciones.max_emR and record.emR > record.restricciones.min_emR)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: emR"
                continue

            if (
                    (record.restricciones.max_epS == 0 and record.restricciones.min_epS ==0 )
                or
                    (record.epS < record.restricciones.max_epS and record.epS > record.restricciones.min_epS)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: epS"
                continue

            if (
                    (record.restricciones.max_emS == 0 and record.restricciones.min_emS ==0 )
                or
                    (record.emS < record.restricciones.max_emS and record.emS > record.restricciones.min_emS)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: emS"
                continue

            if (
                    (record.restricciones.max_epT == 0 and record.restricciones.min_epT ==0 )
                or
                    (record.epT < record.restricciones.max_epT and record.epT > record.restricciones.min_epT)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: epT"
                continue

            if (
                    (record.restricciones.max_emT == 0 and record.restricciones.min_emT ==0 )
                or
                    (record.emT < record.restricciones.max_emT and record.emT > record.restricciones.min_emT)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: emT"
                continue

            if (
                    (record.restricciones.max_epRST == 0 and record.restricciones.min_epRST ==0 )
                or
                    (record.epRST < record.restricciones.max_epRST and record.epRST > record.restricciones.min_epRST)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: epRST"
                continue

            if (
                    (record.restricciones.max_emRST == 0 and record.restricciones.min_emRST ==0 )
                or
                    (record.emRST < record.restricciones.max_emRST and record.emRST > record.restricciones.min_emRST)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: emRST"
                continue

            if (
                    (record.restricciones.max_Q1 == 0 and record.restricciones.min_Q1 ==0 )
                or
                    (record.Q1 < record.restricciones.max_Q1 and record.Q1 > record.restricciones.min_Q1)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: Q1"
                continue

            if (
                    (record.restricciones.max_Q2 == 0 and record.restricciones.min_Q2 ==0 )
                or
                    (record.Q2 < record.restricciones.max_Q2 and record.Q2 > record.restricciones.min_Q2)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: Q2"
                continue

            if (
                    (record.restricciones.max_Q3 == 0 and record.restricciones.min_Q3 ==0 )
                or
                    (record.Q3 < record.restricciones.max_Q3 and record.Q3 > record.restricciones.min_Q3)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: Q3"
                continue

            if (
                    (record.restricciones.max_Q4 == 0 and record.restricciones.min_Q4 ==0 )
                or
                    (record.Q4 < record.restricciones.max_Q4 and record.Q4 > record.restricciones.min_Q4)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: Q4"
                continue

            if (
                    (record.restricciones.max_EcR == 0 and record.restricciones.min_EcR ==0 )
                or
                    (record.EcR < record.restricciones.max_EcR and record.EcR > record.restricciones.min_EcR)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: EcR"
                continue

            if (
                    (record.restricciones.max_EcS == 0 and record.restricciones.min_EcS ==0 )
                or
                    (record.EcS < record.restricciones.max_EcS and record.EcS > record.restricciones.min_EcS)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: EcS"
                continue

            if (
                    (record.restricciones.max_EcT == 0 and record.restricciones.min_EcT ==0 )
                or
                    (record.EcT < record.restricciones.max_EcT and record.EcT > record.restricciones.min_EcT)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: EcT"
                continue

            if (
                    (record.restricciones.max_EcRST == 0 and record.restricciones.min_EcRST ==0 )
                or
                    (record.EcRST < record.restricciones.max_EcRST and record.EcRST > record.restricciones.min_EcRST)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: EcRST"
                continue

            if (
                    (record.restricciones.max_Einv_tot == 0 and record.restricciones.min_Einv_tot ==0 )
                or
                    (record.Einv_tot < record.restricciones.max_Einv_tot and record.Einv_tot > record.restricciones.min_Einv_tot)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: Einv_tot"
                continue

            if (
                    (record.restricciones.max_inversor_1 == 0 and record.restricciones.min_inversor_1 ==0 )
                or
                    (record.inversor_1 < record.restricciones.max_inversor_1 and record.inversor_1 > record.restricciones.min_inversor_1)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: inversor_1"
                continue

            if (
                    (record.restricciones.max_inversor_2 == 0 and record.restricciones.min_inversor_2 ==0 )
                or
                    (record.inversor_2 < record.restricciones.max_inversor_2 and record.inversor_2 > record.restricciones.min_inversor_2)
                ):
                record.estado = "correcto"
            else:
                record.estado = "error: inversor_2"
                continue



#usado para generar el codigo de validación
#for i in [epR,emR,epS,emS,epT,emT,epRST,emRST,Q1,Q2,Q3,Q4,EcR,EcS,EcT,EcRST,Einv_tot,inversor_1,inversor_2]:
#   print(s.format(i))
"""
if (
        (record.restricciones.max_{0} == 0 and record.restricciones.min_{0} ==0 )
    or 
        (record.{0} < record.restricciones.max_{0} and record.{0} > record.restricciones.min_{0})
    ):
    record.estado = "correcto"
else:
    record.estado = "error: {0}"
    continue """