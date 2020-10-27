# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    """
    Create BOM associated to the SO. 
    """
    def create_product_template(self):
        prod_template = self.env['product.template']
        #category_id = 
        for rec in self:
            product_name = rec.name + '-' + rec.description
            product = prod_template.create({
                'name': product_name,
                'purchase_ok': False,
                'type': 'product',
                
            })
    
    def action_create_mrp(self):
        bom = self.env["mrp.bom"]
        
            
        
    