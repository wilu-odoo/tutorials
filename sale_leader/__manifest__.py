# -*- coding: utf-8 -*-
{
    'name': "Sale Leader",

    'summary': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'description': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Tutorials/SaleLeader',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base','sale','sales_team'],

    'data': [
        'security/sale_leader_security.xml',
    ],
    'assets': {


    },
    'license': 'AGPL-3'
}
