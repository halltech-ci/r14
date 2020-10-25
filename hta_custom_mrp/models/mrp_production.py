# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MrpProduction(models.Model):
    _inherit = "mrp.production"
    
    #sale_order = fields.Many2one('sale.order', string="Devis")
    description = fields.Text("Description")