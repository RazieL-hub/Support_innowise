from config.celery import app
from authentication.service import send


@app.task
def send_activation_email(user_email):
    send(user_email)
