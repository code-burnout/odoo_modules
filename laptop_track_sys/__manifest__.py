# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'BakerTilly Laptop Tracking System',
    'version' : '21.0.1',
    'summary': 'System for tracking Bakertilly laptops',
    'sequence': -100,
    'description': """This is a system which logs laptops at BakerTilly from its repairs allocation and costings""",
    'category': 'Accounting/Accounting',
    'website': 'https://cyber.sys/hospitial',
    'depends' : ['mail'],
    'data': [
    #security -- data -- views --reports
        'data/data.xml',
        'security/ir.model.access.csv',
    'views/main_laptop_views.xml',
    'views/owner_views.xml',
    'views/ownership_details_views.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

