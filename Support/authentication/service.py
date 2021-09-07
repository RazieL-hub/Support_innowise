from django.core.mail import send_mail

def send(user_email):
    send_mail('TEST SUBJECT', 'TEST MESSAGE', 'sachukantonytest@gmail.com', [user_email], fail_silently=False)