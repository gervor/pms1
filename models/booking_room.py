from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class BookingRoom(models.Model):
    _name = 'pms1.booking_room'
    _description = 'BookingRoom'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    booking_id = fields.Many2one('pms1.booking', string="Booking", required=True, ondelete='cascade')
    room_id = fields.Many2one('pms1.room', string="Room", required=True, ondelete='cascade')
    booking_room_guest_ids = fields.One2many('pms1.booking_room_guest', 'booking_room_id', string="Guests in Room")

    guest_display = fields.Char(string="Guests", compute="_compute_guest_display")

    @api.depends('booking_room_guest_ids')
    def _compute_guest_display(self):
        for record in self:
            record.guest_display = ', '.join(guest.full_name for guest in record.booking_room_guest_ids.mapped('guest_id'))

    @api.onchange('booking_room_guest_ids')
    def _onchange_booking_room_guest_ids(self):
        _logger.info(f"ONCHANGE: _onchange_booking_room_guest_ids")
        for record in self:
            record.booking_id._setBookedGuests()