from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class TicketCategory(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'ticketcategory'
        verbose_name_plural = 'ticketcategorys'

    def __str__(self):
        return self.category


class Subcategory(models.Model):
    subcategory = models.CharField(max_length=100)
    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategory'


class Ticket(models.Model):
    class TicketStatus(models.TextChoices):
        new = 'new', _('New')
        in_work = 'in_work', _('In_work')
        close = 'close', _('Close')
        error = 'error', _('Error')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible')
    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    ticket_status = models.CharField(max_length=80, choices=TicketStatus.choices, default='new')

    text = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.category} {self.ticket_status} {self.date_created}'

    class Meta:
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'


class Comment(models.Model):
    class Event(models.TextChoices):
        new_comment = 'new_comment', _('New_comment')
        wait_response = 'wait_response', _('Wait_response')
        transfer_responsible = 'transfer_responsible', _('Transfer_responsible')

    event = models.CharField(max_length=120, choices=Event.choices, default='new_comment')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    text_comment = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.date_created} '

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
