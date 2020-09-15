# -*- coding: utf-8 -*-
from odoo import http

# class FitsCustomEmployee(http.Controller):
#     @http.route('/fits_custom_employee/fits_custom_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fits_custom_employee/fits_custom_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fits_custom_employee.listing', {
#             'root': '/fits_custom_employee/fits_custom_employee',
#             'objects': http.request.env['fits_custom_employee.fits_custom_employee'].search([]),
#         })

#     @http.route('/fits_custom_employee/fits_custom_employee/objects/<model("fits_custom_employee.fits_custom_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fits_custom_employee.object', {
#             'object': obj
#         })