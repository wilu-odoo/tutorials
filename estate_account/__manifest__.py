# -*- coding: utf-8 -*-
{
    'name': "Estate Account",

    'summary': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'description': """
        "The first step of module creation is to create its directory. In the tutorials directory, add a new directory estate."
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Tutorials/EstateAccount',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base','estate','account'],

    'data': [
        'report/estate_account_report.xml',
        'report/custom_invoice_report.xml',
    ],
    'assets': {


    },
    'license': 'AGPL-3'
}
