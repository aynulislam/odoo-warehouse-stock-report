# -*- coding: utf-8 -*-
{
    'name': 'Stock Inventory Report | Stock Inventory Aging Report',
    'description': """
          Stock Inventory Report
    """,
    'summary': 'Stock Inventory Report',
    'version': '1.0',
    'category': 'Inventory',
    'author': 'MaplesHub Solutions.',
    'company': 'MaplesHub Solutions.',
    'maintainer': 'MaplesHub Solutions.',
    'website': "https://www.mapleshub.com",
    'depends': [
        'stock',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Report
        'report/stock_report_pdf.xml',
        # Wizard
        'wizard/stock_report_wizard.xml',
        # Views
        'views/menus.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
