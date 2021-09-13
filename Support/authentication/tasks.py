from config.celery import app
from authentication.service import send


@app.task
def send_activation_email(email_subject, email_body, email_from, email_to):
    send(email_subject, email_body, email_from, email_to)
