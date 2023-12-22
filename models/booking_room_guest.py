from odoo import api, fields, models, _

import json
import logging
_logger = logging.getLogger(__name__)

class BookingRoomGuest(models.Model):
    _name = 'pms1.booking_room_guest'
    _description = 'BookingRoomGuest'
    _rec_name = 'full_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    booking_room_id = fields.Many2one('pms1.booking_room', string="Booking Room", required=True)
    guest_id = fields.Many2one('pms1.guest', string="Guest", required=True)
    departure_date = fields.Date("Departure Date")

    full_name = fields.Char(string="Full Name", compute="_compute_full_name", store=True)

    @api.depends('guest_id')
    def _compute_full_name(self):
        for record in self:
            if record.guest_id:
                record.full_name = record.guest_id.full_name

    @api.onchange('guest_id')
    def _onchange_guest_id(self):
        for record in self:
            _logger.info(f"ONCHANGE: {record.guest_id}")