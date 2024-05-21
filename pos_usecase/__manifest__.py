# -*- coding: utf-8 -*-
{
    'name': "POS Use Case",

    'summary': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'description': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Tutorials/POSuseCase',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base','point_of_sale', 'pos_sale'],

    'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_usecase/static/src/**/*'
        ]

    },
    'license': 'AGPL-3'
}
