# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    _SALE_ORDER_DOMAINE = [('fm', 'FABRICATION MECANIQUE'),
                          ('cm', 'CONSTRUCTION METALLIQUE'),
                          ('gc', 'GENIE CIVILE'),
                          ('ct', 'CHAUDRONNERIE TUYAUTERIE'),
                          ('em', 'ELECTROMECANIQUE'),
                          ('bt', 'BATIMENT'),
                          ('ra', 'RECTIFICATION AUTOMOBILE'),
                          ('mi', 'MAINTENANCE INDUSTRIELLE'),
                          ('me', 'MAINTENANCE ELECTROMECANIQUE'),
                          ('mm', 'MAINTENANCE MECANIQUE'),
                          ('cu', 'CONSTRUCTION USINE'),
                          ('ep', 'ETUDES DE PROJET')
    ]
    
    project_id = fields.Many2one("project.project", "Project", ondelete= "cascade")
    project_code = fields.Char("Code Projet", related='project_id.project_code')
    description = fields.Text("Description")
    signed_user = fields.Many2one("res.users", string="Signed In User", readonly=True, default= lambda self: self.env.uid)
    sale_order_recipient = fields.Char("Destinataire")
    sale_order_type = fields.Selection(_SALE_ORDER_DOMAINE, string="Domaine", required=True, index=True, default='fm')
    
    '''
    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            if vals.get('sale_order_type', 'fm'):
                domaine_code = vals.get('sale_order_type')
                next_code = '{0}.{1}.{2}'.format('sale',domaine_code, 'sequence')
                seq_date = None
                if 'date_order' in vals:
                    seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
                vals['name'] = self.env['ir.sequence'].next_by_code(next_code, sequence_date=seq_date) or _('New')

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist.id)
        result = super(SaleOrder, self).create(vals)
        return result'''