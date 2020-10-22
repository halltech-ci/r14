# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSaleMrp(http.Controller):
#     @http.route('/hta_sale_mrp/hta_sale_mrp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale_mrp/hta_sale_mrp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale_mrp.listing', {
#             'root': '/hta_sale_mrp/hta_sale_mrp',
#             'objects': http.request.env['hta_sale_mrp.hta_sale_mrp'].search([]),
#         })

#     @http.route('/hta_sale_mrp/hta_sale_mrp/objects/<model("hta_sale_mrp.hta_sale_mrp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale_mrp.object', {
#             'object': obj
#         })
