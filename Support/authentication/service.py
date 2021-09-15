from django.core.mail import send_mail



def send(email_subject, email_body, email_from, email_to):
    send_mail(email_subject, email_body, email_from, [email_to], fail_silently=False)
