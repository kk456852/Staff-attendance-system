from flask_mail import Message
from flask import render_template
from .. import mail

prefix = '[SAS]'


def send_mail(to, subject, template, **kwargs):
    msg = Message(subject=prefix + ' ' + subject, recipients=[to])
    msg.body = ' '
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
