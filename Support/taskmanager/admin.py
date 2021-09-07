from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from taskmanager.models import Ticket, TicketCategory, Subcategory, Comment


class TicketAdminForm(forms.ModelForm):
    text = forms.CharField(label="Описание", widget=CKEditorWidget())

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketAdmin(admin.ModelAdmin):
    form = TicketAdminForm


admin.site.register(TicketCategory)
admin.site.register(Subcategory)
admin.site.register(Ticket)

admin.site.register(Comment)
