# Copyright 2022 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Line Pricelist Sale',
    'summary': 'Set in account invoice lines'
    ' the pricelist set in sale order lines',
    'version': '12.0.1.0.0',
    'development_status': 'Beta',
    'category': 'Generic Modules/Accounting',
    'website': 'https://github.com/OCA/sale-workflow',
    'author': 'PlanetaTIC, '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'account',
        'sale_order_line_pricelist',
    ],
    'data': [
        'views/account_invoice_view.xml',
    ],
}
