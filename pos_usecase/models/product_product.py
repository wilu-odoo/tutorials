from odoo import models, fields, api

class ProductProductInherited(models.Model):
    _inherit = 'product.product'

    @api.model
    def get_product_info_pos(self, price, quantity, pos_config_id):
        product_info = super(ProductProductInherited, self).get_product_info_pos(price, quantity, pos_config_id)
        weight = self.weight
        volume = self.volume
        product_info['weight'] = weight
        product_info['volume'] = volume

        return product_info



#super(InheritedEstateProperty, self).action_do_sold()