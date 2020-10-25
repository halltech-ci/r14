# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProjectProject(models.Model):
    _inherit = "project.project"
    
    sale_order_ids = fields.One2many("sale.order", "project_id", string="Sale Orders")
    project_code = fields.Char(string='Code Projet', required=True, readonly=True, copy=False, default= lambda self: _('New'))