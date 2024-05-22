from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Filled with bunch of estate properties offers"
    _order = "price desc"

    _sql_constraints = [
    ('positive_price', 'CHECK(price > 0)', 'Price should be a positive number.'),
    ]

    price = fields.Float("Price")
    status = fields.Selection(
        string='Status',
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy = False
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property",  string="Property", required=True)
    validity = fields.Integer("Validity", default = 7)
    date_deadline = fields.Date("Deadline Date", compute = "_compute_validity_date", inverse = "_inverse_validity_date")
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", store=True)

    
    @api.depends("validity")
    def _compute_validity_date(self):
        for record in self:
            record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_validity_date(self):
        for record in self:
            record.validity = (record.date_deadline - fields.Date.today()).days

    def action_do_accept(self):
        for record in self:
            for other in record.property_id.offer:
                if other.status != 'refused':
                    other.status = 'refused'
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id
            record.property_id.state = 'offer_accepted'
        return True

    def action_do_refuse(self):
        for record in self:
            record.status = 'refused'
            record.property_id.selling_price = 0
            record.property_id.buyer = None
        return True
    
    @api.model
    def create(self, vals):
        if self.env['estate.property'].browse(vals['property_id']).state == 'sold':
            raise UserError(("Cannot create offer on sold properties"))
        best = self.env['estate.property'].browse(vals['property_id']).best_offer
        if best > vals['price']:
            raise UserError(("New offer cannot have lower price than existing offers"))
        self.env['estate.property'].browse(vals['property_id']).state = 'offer_received'
        return super().create(vals)

