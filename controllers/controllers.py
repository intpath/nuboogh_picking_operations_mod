# -*- coding: utf-8 -*-
# from odoo import http


# class NubooghPickingOperationsMod(http.Controller):
#     @http.route('/nuboogh_picking_operations_mod/nuboogh_picking_operations_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nuboogh_picking_operations_mod/nuboogh_picking_operations_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nuboogh_picking_operations_mod.listing', {
#             'root': '/nuboogh_picking_operations_mod/nuboogh_picking_operations_mod',
#             'objects': http.request.env['nuboogh_picking_operations_mod.nuboogh_picking_operations_mod'].search([]),
#         })

#     @http.route('/nuboogh_picking_operations_mod/nuboogh_picking_operations_mod/objects/<model("nuboogh_picking_operations_mod.nuboogh_picking_operations_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nuboogh_picking_operations_mod.object', {
#             'object': obj
#         })
