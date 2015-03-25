{
    'name': 'Suppress OOF Replies',
    'version': '0.1',
    'category': 'Social Network',
    'summary': ' Suppress OOF replies from Exchange servers',
    'description': """
Suppress OOF replies from Exchange servers
==========================================
OpenERP v 8.0 and above suppresses out-of-office replies from Exchange servers by default.
This is a workaround for OpenERP v 7.0
    """,
    'author': 'Vadim <vadim@based.at>',
    'website': 'http://based.at',
    'depends': ['mail'],
    'data': ['mail_group_view.xml'],
    'installable': True,
}
