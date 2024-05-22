from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateModel(models.Model):
    _name = "estate.property"
    _description = "Filled with bunch of estate properties"
    _order = "id desc"

    _sql_constraints = [
    ('positive_expected_price', 'CHECK(expected_price > 0)', 'Expected Price should be a positive number.'),
    ('positive_selling_price', 'CHECK(selling_price >= 0)', 'Selling Price should be a positive number.'),
    ]


    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date("Date Availability", default = fields.Date.today() + relativedelta(months=3),)
    expected_price = fields.Float('Expected Price', required=True)
    best_offer = fields.Float('Best Offer', compute="_compute_best_offer")
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedroom', default=2)
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    active = fields.Boolean('Active', default = True)
    state = fields.Selection(
        selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'), ('canceled', 'Canceled')],
        default = 'new'
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesperson = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    buyer = fields.Many2one("res.partner", string="Buyer")
    tags = fields.Many2many("estate.property.tag", string ="Tags")
    offer = fields.One2many("estate.property.offer", "property_id")
    total_area = fields.Integer("Total Area" , compute="_compute_total_area")
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area


    @api.depends("offer")
    def _compute_best_offer(self):
        for record in self:
            if record.offer:
                record.best_offer = max(record.offer.mapped("price"))
            else:
                record.best_offer = 0
        
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden == False:
            self.garden_area = 0
            self.garden_orientation = False
        else:
            self.garden_area = 10
            self.garden_orientation = "north"

    def action_do_cancel(self):
        for record in self:
            if record.state != 'sold':
                record.state = 'canceled'
            else:
                raise UserError(("Sold properties cannot be canceled."))
        return True

    def action_do_sold(self):
        for record in self:
            if record.state != 'canceled':
                record.state= 'sold'
            else:
                raise UserError(("Canceled properties cannot be sold"))
        return True
    
    @api.constrains('state','offer')
    def _check_accepted_offer(self):
        for record in self:
            if record.state == 'sold' and not record.offer.filtered(lambda offer: offer.status == 'accepted'):
                raise UserError('Cannot sell a property with no accepted offers.')

    @api.constrains('expected_price','selling_price')
    def _check_prices(self):
        for record in self:
            if float_compare(record.expected_price * 0.9, record.selling_price, precision_digits=2) == 1 and not float_is_zero(record.selling_price, precision_digits=2):
                raise ValidationError("Selling Price is lower than 0.9 of expected price")

    @api.ondelete(at_uninstall=False)
    def _unlink_if_property_new_or_canceled(self):
        for record in self:
            if record.state not in ("new", "canceled"):
                raise UserError("Only new and canceled state properties can be deleted")