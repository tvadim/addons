# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Vadim (<http://based.at>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv


class MailGroup(osv.Model):
    """ Add boolean field to suppress Out-Of-Office replies from Exchange servers """
    _inherit = 'mail.group'

    _columns = {
        'suppress_oof':
            fields.boolean('Suppress OOF Replies',
                           help="Check this option to ask Exchange servers do not sent Out-Of-Office replies to messages in this group")
    }

    _defaults = {
        'suppress_oof': True,
    }
