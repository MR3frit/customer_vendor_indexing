# -*- coding: utf-8 -*-
{
    'name': 'Customer And Vendor Indexing',
    'version': '1.0',
    'author': 'Eng / Mahmoud Ossman',
    'category': 'Contacts, Products',
    'depends': ['base', 'mail', 'account', 'contacts', 'sale'],
    'description': """ """,
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
