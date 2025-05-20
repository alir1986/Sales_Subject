from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    memo = fields.Text(string='Memo', default= "Subject" , readonly=False)
        