
# -*- coding: utf-8 -*-
{
    'name': 'Customer And Vendor Indexing',
    'version': '16.0.1.0.0',
    'author': 'Vipdoo - Eng / Mahmoud Ossman',
    'category': 'Contacts, Products',
    'summary': 'Contact Us : +201222842875',
    'license': 'LGPL-3',
    'website': 'https://vipdooegypt.com/',
    'depends': ['base', 'mail', 'account', 'contacts', 'sale'],
    'description': """ Adding Sequance For Customers And Vendors """,
    'data': [
        'views/res_partner_views.xml',
        'views/account_move.xml',
        'views/sale_order.xml',
        'data/ir_sequence_data.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'assets': {
    },
}
