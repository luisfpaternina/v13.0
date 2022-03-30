# -*- coding: utf-8 -*-
{
    'name': "stock picking extended",

    'summary': """
        Este modulo agrega una ventana de dialogo en el boton cancelar en las transferencias de inventario""",

    'author': "Nybblegroup",

    'website': "www.nybblegroup.com",

    'category': 'Operations/Inventory',

    'version': '13.0.0.1.3',

    'depends': [
        'stock',
    ],

    'data': [

        "views/stock_picking.xml",
    ],
    
    'installable': True,
}
