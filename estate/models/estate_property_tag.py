from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Filled with bunch of estate properties tag"
    _order = "name asc"

    _sql_constraints = [
    ('unique_tag', 'UNIQUE(name)', 'tags name should be unique'),
    ]

    name = fields.Char('Name', required=True)
    color = fields.Integer('Color')

