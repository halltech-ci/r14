# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import AccessError, UserError
from odoo.tools import float_compare

class CustomProduction(models.Model):
    """Custom Manufacturing Order"""
    _name = "custom.production"
    _description = 'Manufacturing Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    #sale_order = fields.Many2one('sale.order', string="Devis")
    name = fields.Char('Reference', copy=False, readonly=True, default=lambda x: _('New'))
    description = fields.Text("Description")
    sale_order = fields.Many2one('sale.order', string='Sale Order')
    
    
class CsutomProductionLine(model.Models):
    _name = "custom.production.line"
    
    
    
    