{
    'name': 'norauto custom reports',

    'version': '13.0.0.0',

    'author': "Nybblegroup",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.nybblegroup/",

    'category': 'reports',

    'depends': [

        'sale_management',
        'base',

    ],

    'data': [
       
        #'security/security.xml',
        #'security/ir.model.access.csv',
       'reports/sale_order_report.xml',
        #'views/res_partner.xml',
        
    ],
    'installable': True
}

