# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    description = fields.Text('Description')
    """
    Create BOM associated to the SO. 
    """
    def action_create_bom(self):
        #create product
        prod = self.env['product.template']
        for record in self:
            product_name = record.description
            route_id = self.env['stock.location.route'].search([('name', '=', 'Manufacture')]).id
            route = []
            route_ids = route.append(route_id)
            prod.create({
                'name': product_name,
                'type': 'product',
                'purchase_ok': False,
                'categ_id': 1,
                'route_ids': route_ids
            })
    
    
    def create_product_template(self):
        prod_template = self.env['product.template']
        #category_id = 
        for rec in self:
            product_name = rec.name + '-' + rec.description
            product = prod_template.create({
                'name': product_name,
                'purchase_ok': False,
                'type': 'product',
                #categ_id = 1
                
            })
            
    def create_product_category(self):
        categ = self.env['product.category']
        categ_name = self.env['product.category'].search([('name', '=', 'Manufacture')])
        if not categ_name:
            categ.create({
                'name': 'Manufacture',
                'parent_id': 1,
                'property_cost_method': 'standard',
                'propert_valuation': 'namual_periodic'
            })
            
    #@api.model
    def action_create_mrp(self, bom_id):
        self.create_product_category
        bom = self.env["mrp.bom"]
        
            
        
    