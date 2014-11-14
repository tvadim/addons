# -*- coding: utf-8 -*-
__author__ = 'vadim'

from openerp.osv import fields, osv


class ResUsers(osv.Model):
    _inherit = 'res.users'

    _columns = {
        'notification_receive_copy':
            fields.boolean('Bcc Sent Messages',
                           help="If this option is checked you will receive a blind carbon copy of sent messages to your email address")
    }

    _defaults = {
        'notification_receive_copy': False,
    }
