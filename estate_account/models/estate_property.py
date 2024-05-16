from odoo import models, fields, Command

class InheritedEstateProperty(models.Model):
    _inherit = "estate.property"

    def action_do_sold(self):
        self.check_access_rights('write')
        self.check_access_rule('write')
        # self.env['account.move'].check_access_rights('write')
        # self.env['account.move'].check_access_rule('write')
        print(" reached ".center(100, '='))
        self.env['account.move'].sudo().create({
            'move_type': 'out_invoice',
            'partner_id': self.buyer.id,
            'name': "Property Selling",
            'invoice_line_ids': [
                Command.create({
                    "name": self.name,
                    "quantity": 1,
                    "price_unit": (self.selling_price * 0.06 + 100)
                })
            ]
        })

        return super(InheritedEstateProperty, self).action_do_sold()