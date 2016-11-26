from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from .emails import send_reg_email
from django.conf import settings

logger = get_task_logger(__name__)


@shared_task(name='send_reg_email_task')
def send_reg_email_task(name, email):
    logger.info('Sent email.')
    return send_reg_email(name, email)


@shared_task(name='send_to_telegram_task')
def send_to_telegram_task(name, email):
    url = 'https://api.telegram.org/'
    bot_token = settings.BOT_TOKEN
    chat_id = 'chat_id=' + settings.CHAT_ID
    text = 'Name: ' + name + ' Email: ' + email
    method_name = '/sendMessage'
    send = url + 'bot' + bot_token + method_name + '?' + chat_id + '&text=' + text
    r = requests.post(send)
    logger.info(r)
