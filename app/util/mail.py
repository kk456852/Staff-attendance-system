from flask import current_app, render_template
from flask_mail import Message

from .. import mail
from . import executor

prefix = '[SAS]'


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            app.logger.exception(e)


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=prefix + ' ' + subject, recipients=[to])
    msg.body = ''
    msg.html = render_template(template, **kwargs)
    executor.submit(send_async_email, app, msg)
