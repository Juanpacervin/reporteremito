# -*- coding: utf-8 -*-
{
    'name': "Reporte de Remitos Preimpresos",
    'description': """
        Reporte para remitos preimpresos
    """,
    'author': "Waikiservicios",
    'website': "",
    'version': '1.0',
    'category': 'Stock',
    'version': '0.1',
    'depends': ['stock'],
    'data': [
        'report/report_remito.xml',
        'report/report_remito_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
