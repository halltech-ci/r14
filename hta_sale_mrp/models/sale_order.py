# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
   
    def action_create_mrp(self):
        bom = self.env["mrp.bom"]
        
    