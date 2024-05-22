from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged
from odoo.tests.common import Form

# The CI will run these tests after all the modules are installed,
# not right after installing the one defining it.
@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        # add env on cls and many other things
        super(EstateTestCase, cls).setUpClass()

        # create the data for each tests. By doing it in the setUpClass instead
        # of in a setUp or in each test case, we reduce the testing time and
        # the duplication of code.
        cls.estate_property_type_id2 = cls.env.ref('estate.estate_property_type_id2')
        cls.base_res_partner_12 = cls.env.ref('base.res_partner_12')
        cls.properties = cls.env['estate.property'].create({
            'name': 'Small Big Villa',
            'property_type_id': cls.estate_property_type_id2.id,
            'state': 'new',
            'description': 'A nice and big villa',
            'postcode': '12345',
            'date_availability': '2020-02-02',
            'expected_price': 1600000,
            'bedrooms': 6,
            'living_area': 100,
            'facades': 4,
            'garage': True,
            'garden': True,
            'garden_area': 1000,
            'garden_orientation': 'south',
            'offer': [(0, 0, {
                'partner_id': cls.base_res_partner_12.id,
                'price': 1600000,
                'validity': 14
            })],
        })

    def test_garden_onchange(self):
        with Form(self.properties) as form:
            form.garden = False
            form.save()
            self.assertRecordValues(self.properties, [
           {'name': 'Small Big Villa', 'garden': False},
            ])

            self.assertRecordValues(self.properties, [
           {'name': 'Small Big Villa', 'garden_area': 0},
            ])

    def test_creation_area(self):
        """Test that the total_area is computed like it should."""
        self.properties.living_area = 20
        self.assertRecordValues(self.properties, [
           {'name': 'Small Big Villa', 'total_area': 1020},
        ])


    def test_action_sell(self):
        """Test that everything behaves like it should when selling a property."""
        with self.assertRaises(UserError):
            self.properties.action_do_sold()
        self.properties.offer.action_do_accept()
        self.properties.action_do_sold()
        self.assertRecordValues(self.properties, [
           {'name': 'Small Big Villa', 'state': 'sold'},
        ])

        