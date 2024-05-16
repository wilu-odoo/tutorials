# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'description': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Real Estate/Brokerage',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base'],

    'data': [
        'security/estate_property_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
        'views/res_users_views.xml',
        'report/estate_property_offer_templates.xml',
        'report/estate_property_offer_reports.xml',
        'data/master_data.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'license': 'AGPL-3'
}
