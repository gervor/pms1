from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class Room(models.Model):
    _name = 'pms1.room'
    _description = 'Room'
    _rec_name = 'room_no'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    room_no = fields.Char(string='Room No', required=True, tracking=True)
    active = fields.Boolean(string="Active", default=True)

    #booking_ids = fields.Many2many('pms1.booking', string="Bookings")

    @api.model
    def get_active_rooms(self):
        # Logic to fetch bookings between start_date and end_date
        rooms = self.search([('active', '=', True)])

        return rooms.read(['id', 'room_no'])