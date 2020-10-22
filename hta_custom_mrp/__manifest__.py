# -*- coding: utf-8 -*-
{
    'name': "hta_custom_mrp",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ATCHE Maurice",
    'website': "http://www.halltech-africa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing/Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_setup',
                'mrp',
                'sale_management',
               ],

    # always loaded
    'data': [
         #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/mrp_production_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
