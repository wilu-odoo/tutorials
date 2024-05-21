# from odoo import models, fields, api

# class CrmTeamInherited(models.Model):
#     _inherit = 'crm.team'

#     @api.model_create_multi
#     def create(self, vals_list):
#         for values in vals_list:
#             teams = super(CrmTeamInherited, self.with_context(mail_create_nosubscribe=True)).create(vals_list)
#             if(values['user_id']!=False):
#                 user = self.env['res.users'].browse(values['user_id'])
#                 user.write({'groups_id': [(4, 75)]})
#         return teams

#     def write(self, values):
#         res = super(CrmTeamInherited, self).write(values)
#         if(values['user_id']!=False):
#             user = self.env['res.users'].browse(values['user_id'])
#             user.write({'groups_id': [(4, self.env['res.groups'].search([
#             ('name', 'ilike', 'Team Leader'),
#             ('category_id', '=', 9)
#             ]).id )]})
#         return res
