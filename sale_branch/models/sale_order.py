from odoo import api, models, fields

class InheritedEstateProperty(models.Model):
    _inherit = "sale.order"

    branch_id = fields.Many2one('sale.branch', 'Branch')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals['branch_id']:
                branch_code = self.env['sale.branch'].browse(vals['branch_id']).code
                #vals['name']  =  self.env['ir.sequence'].search([('code', '=', branch_code)], limit=1).name
                vals['name']  =  self.env['ir.sequence'].next_by_code(branch_code)
        return super().create(vals_list)