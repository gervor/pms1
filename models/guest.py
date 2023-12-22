from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)

class Guest(models.Model):
    _name = 'pms1.guest'
    _description = 'Guest'
    _rec_name = 'full_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    firstname = fields.Char(string='Firstname', required=True, tracking=True)
    lastname = fields.Char(string="Lastname", tracking=True)
    full_name = fields.Char(string="Full Name", compute="_compute_full_name", store=True)

    date_of_birth = fields.Date(string="Date of birth", tracking=True)
    email = fields.Char(string='Email')

    @api.depends('firstname', 'lastname')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.firstname or ''} {record.lastname or ''}".strip()