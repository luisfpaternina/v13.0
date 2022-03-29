# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_transfer = fields.Boolean(
        string="Is transfer",
        related="picking_type_id.is_transfer")
    location_dest_id = fields.Many2one(
        'stock.location',
        string="Location dest")


    @api.onchange('picking_type_id','location_dest_id')
    def domain_location_dest(self):
        # Función para aplicar dominio en ubicación destino
        for record in self:
            if record.picking_type_id.is_transfer and record.picking_type_id:
                return {'domain': {'location_dest_id': [('is_transfer', '=', True)]}}
            else:
                return {'domain': {'location_dest_id': []}}

