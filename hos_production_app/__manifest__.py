# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Production Application',
    'version' : '14.0.1',
    'summary': 'Invoices & Payments',
    'sequence': -100,
    'description': """this is for monitoring vad production systems to manage its flow """,
    'category': 'Accounting/Accounting',
    'website': 'https://cyber.sys/hospitial',
    'depends' : ['sale','mail','account'],
    'data': [
    #security -- data -- views --reports
        'security/production_security.xml',
        'security/ir.model.access.csv',
    'views/main_prod_app.xml',
    'views/add_files_sales.xml',
    'views/stage_views.xml',
    'report/english_options.xml',
    'report/english_report.xml',
    'report/norwegian_reports.xml',

    # add this line
    'report/packging_list.xml',
    'report/invoives_options.xml',
    'report/production_report.xml',
    'report/prod_report.xml',
    'report/invoices_report.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

