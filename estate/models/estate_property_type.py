from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Filled with bunch of estate properties type"
    _order = "sequence, name asc"

    name = fields.Char('Name', required=True)
    sequence = fields.Integer('Sequence', default = 1, help="Used to order property type based on the most used type")
    property_ids = fields.One2many("estate.property", 'property_type_id', string= "Properties")
    offer_ids = fields.One2many("estate.property.offer", 'property_type_id')
    offer_count = fields.Integer('Offer Count', compute="_compute_offer_count")

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)