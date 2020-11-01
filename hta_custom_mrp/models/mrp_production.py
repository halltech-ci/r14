# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MrpProduction(models.Model):
    _inherit = "mrp.production"
    
    sale_order = fields.Many2one('sale.order', string="Commande")
    description = fields.Text("Description")
    
    """def create_mrp_bom(self, order):
        '''create product template for coresponding sale_order'''
        product_name = order.description
        product = self.env['product.product']
        prod_templ = product.create({
                'name': product_name,
                'type': 'product',
                'purchase_ok': False,
                'categ_id': 1,
                #'route_ids': route_ids
            })
            self.sale_mrp_product = prod_templ
    def create_mo_from_so(self):
        for record in self:
            if record.sale_order :
                lines = record.sale_order.line_id
    """            
class MrpOrderLine(models.Model):
    _name = "mrp.order.line"
    _description = "MRP order line"
    
    
                
            