from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    customer_po_number = fields.Char(string='Customer PO Number')
    bank_name = fields.Char(string='Bank Name')
    bank_account_number = fields.Char(string='Bank Account Number')
    bank_ifsc_code = fields.Char(string='IFSC Code')
    terms_and_conditions = fields.Text(string='Terms and Conditions', default="Payment should be made within the agreed payment period.\nGoods/services once sold are subject to company terms.\nPlease mention the invoice number while making payment.")