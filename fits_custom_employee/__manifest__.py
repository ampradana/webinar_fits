# -*- coding: utf-8 -*-
{
    'name': "fits_custom_employee",

    'summary': """
        Custom add fields Employee""",

    'description': """
        Latihan Webinar Fits
    """,

    'author': "fits",
    'website': "https://www.fujicon-japan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
