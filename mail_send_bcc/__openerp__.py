{
    'name': 'Send BCC',
    'version': '0.1',
    'category': 'Social Network',
    'summary': 'Send BCC to message originator',
    'description': """
Send BCC to message originator
==============================
Override default behaviour when sending email to partners: send a blind carbon copy to the message originator.
    """,
    'author': 'Vadim <vadim@based.at>',
    'website': 'http://based.at',
    'depends': ['mail'],
    'data': ['res_users_view.xml'],
    'installable': True,
}
