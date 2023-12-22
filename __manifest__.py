# -*- coding: utf-8 -*-
{
    'name' : 'PMS1',
    'version' : '1.0',
    'summary': 'PMS1',
    'sequence': -1,
    'description': """PMS1""",
    'category': 'OWL',
    'depends' : ['base', 'web', 'sale', 'board'],
    'data': [
        'views/booking_room.xml',
        'views/booking_room_guest.xml',
        'views/booking.xml',
        'views/room.xml',
        'views/guest.xml',
        'views/pms1.xml',
        'security/ir.model.access.csv',
        'data/email_templates/booking_confirmation.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'pms1/static/src/components/**/*.js',
            'pms1/static/src/components/**/*.xml',
            'pms1/static/src/components/**/*.scss',
        ],
    },
}