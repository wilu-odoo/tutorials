from odoo import models, fields, api

class PosConfigInherited(models.Model):
    _inherit = 'pos.config'

    congratulatory_text = fields.Char()