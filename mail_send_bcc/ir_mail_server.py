# -*- coding: utf-8 -*-
__author__ = 'vadim'

from openerp.osv import osv
from email.utils import COMMASPACE
from addons.base.ir.ir_mail_server import encode_rfc2822_address_header, extract_rfc2822_addresses


class IrMailServer(osv.Model):
    _inherit = "ir.mail_server"

    def send_email(self, cr, uid, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False,
                   context=None):
        """ Send blind carbon copy to message originator
        """
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        if user.notification_receive_copy:
            bcc_list = extract_rfc2822_addresses(message['Bcc'])
            bcc = user.email or '%s@%s' % (user.alias_name, user.alias_domain) if user.alias_domain else None
            if bcc:
                message['Bcc'] = encode_rfc2822_address_header(COMMASPACE.join(bcc_list + [bcc]))

        return super(IrMailServer, self).send_email(cr, uid, message, mail_server_id, smtp_server, smtp_port,
                                                    smtp_user, smtp_password, smtp_encryption, smtp_debug, context)
