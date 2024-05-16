# -*- coding: utf-8 -*-
{
    'name': "Sale Branch",

    'summary': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'description': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Tutorials/SaleBranch',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base','sale','account'],

    'data': [
        'security/ir.model.access.csv',
        'views/sale_branch_views.xml',
        'views/sale_order_views.xml',
    ],
    'assets': {


    },
    'license': 'AGPL-3'
}
