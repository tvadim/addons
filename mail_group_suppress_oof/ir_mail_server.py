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

from openerp.osv import osv


class IrMailServer(osv.Model):
    _inherit = "ir.mail_server"

    def send_email(self, cr, uid, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False,
                   context=None):
        """ Add 'X-Auto-Response-Suppress':'OOF' header
        """
        context = context or {}
        mail_group = self.pool.get('mail.group')
        model, res_id = context.get('default_model'), context.get('default_res_id')
        if model == 'mail.group' and mail_group.read(cr, uid, res_id, ['suppress_oof'], context=context)['suppress_oof']:
            message.add_header('X-Auto-Response-Suppress', 'OOF')
        return super(IrMailServer, self).send_email(cr, uid, message, mail_server_id, smtp_server, smtp_port,
                                                    smtp_user, smtp_password, smtp_encryption, smtp_debug, context)
