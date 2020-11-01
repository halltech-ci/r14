# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    description = fields.Text('Description')
    sale_mrp_product = fields.Many2one('product.template', ondelete='cascade')
    mrp_bom_id = fields.Many2one("mrp.bom")
    sale_mrp = fields.Many2one('mrp.production')
    
    """
    Create BOM associated to the SO. 
    """
    def create_sale_mrp_product(self, order):
        '''create product template for coresponding sale_order'''
        product_template = self.env['product.template']
        if not order.sale_mrp_product:
            product_name = order.description
            route_id = self.env['stock.location.route'].search([('name', '=', 'Manufacture')]).id
            route = []
            route_ids = route.append(route_id)
            prod_templ = product_template.create({
                'name': product_name,
                'type': 'product',
                'purchase_ok': False,
                'categ_id': 1,
                'route_ids': route_ids
            })
            order.sale_mrp_product = prod_templ
            
    def create_product_bom(self, order):
        bom_id = self.env['product.template'].search([('id', '=', order.sale_mrp_product.id)], limit=1)
        bom = self.env['mrp.bom']
        bom_line = self.env['mrp.bom.line']
        product_ids = []
        lines = order.order_line
        if not order.mrp_bom_id:
            mrp_bom = bom.create({
                'product_tmpl_id': order.sale_mrp_product,
            })
            order.mrp_bom_id = mrp_bom
            for line in lines:
                product_ids.append(line.product_id.id)
                bom_line.create({
                    'product_id': line.product_id,
                    'product_qty': line.product_uom_qty,
                    'bom_id':mrp_bom
                })
                
    #@api.model
    def action_create_mrp(self):
        mo_id = self.env['mrp.production']
        mrp_production = self.env['mrp.production']
        for order in self:
            self.create_sale_mrp_product(order)
            #self.create_product_bom(order)
            if not order.sale_mrp:
                sale_mrp = mrp_production.create({
                    'product_id': order.sale_mrp_product,
                    'bom_id': order.mrp_bom_id
                })
                order.sale_mrp = sale_mrp
        
        
        
            
                
        
            
        
    