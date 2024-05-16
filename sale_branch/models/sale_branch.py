from dateutil.relativedelta import relativedelta
from odoo import api, fields, models

class SaleBranch(models.Model):
    _name = "sale.branch"
    _description = "Filled with branches of a shop"


    name = fields.Char('Name', required=True)
    sequence_id = fields.Many2one('ir.sequence','Sequence ID')
    code = fields.Char('Code')
   

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].create({
            'name': vals['name'],
            'code': vals['code'],
            'prefix' : vals['code'].upper(),
            'padding' : 5
        })
        vals['sequence_id'] = sequence.id 
        return super().create(vals)
