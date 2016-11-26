from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string


def send_reg_email(name, email):
    c = Context({
        'name': name,
        'email': email
    })

    subject = 'Email from Reg Form'
    email_body = render_to_string('email/email_body.txt', c)

    email = EmailMessage(
        subject, email_body, email, settings.EMAIL_TO, [],
        headers={'Reply-To': email}
    )
    return email.send(fail_silently=False)
