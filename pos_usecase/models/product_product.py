from odoo import models, fields, api

class ProductProductInherited(models.Model):
    _inherit = 'product.product'

    def get_product_info_pos(self, price, quantity, pos_config_id):
        res = super().get_product_info_pos(price, quantity, pos_config_id)
        res['weight'] = self.weight
        res['volume'] = self.volume
        return res
