from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class Booking(models.Model):
    _name = 'pms1.booking'
    _description = 'Booking'
    _rec_name = 'booking_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    booking_name = fields.Char(string='Booking Name', compute="_compute_booking_name", store=True)
    arrival_date = fields.Date(string="Arrival Date", tracking=True)
    departure_date = fields.Date(string="Departure Date", tracking=True)

    guest_id = fields.Many2one('pms1.guest', string='Booking Guest')
    booking_room_ids = fields.One2many('pms1.booking_room', 'booking_id', string="Booked Rooms")

    booked_guest_ids = fields.Many2many('pms1.guest', compute='_compute_booked_guest_ids', store=False)

    @api.depends('guest_id')
    def _compute_booking_name(self):
        for record in self:
            record.booking_name = f"{record.guest_id.full_name or ''}".strip()

    def _setBookedGuests(self):
        _logger.info(f"BOOKING ONCHANGE: booking_room_ids")
        for record in self:
            record._compute_booked_guest_ids()


    def _compute_booked_guest_ids(self):
        for record in self:
            guest_ids = record.mapped('booking_room_ids.booking_room_guest_ids.guest_id').ids
            record.booked_guest_ids = guest_ids
            _logger.info(f"BOOKED GUESTS: {record.booked_guest_ids}")  # guest_ids will now be a list of IDs
