from django.contrib import admin
from taskmanager.models import Ticket, TicketCategory, Subcategory, Comments


admin.site.register(TicketCategory)
admin.site.register(Subcategory)
admin.site.register(Ticket)
admin.site.register(Comments)
