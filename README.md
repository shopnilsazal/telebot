# TeleBot
#### A registration app with email and telegram bot notification.
#### Built with Celery and Django.
After an user submit the registration form a notification is sent to email and telegram bot with form data.

## Instructions

* Clone the repository 
* Run `pip install -r requirements.txt`
* Start `redis`
* Start `celery worker` and `celery beat`
* Run `python manage.py runserver`
