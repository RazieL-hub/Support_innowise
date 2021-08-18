from django.urls import path
from taskmanager.views import TicketCreateView, TicketListView, TicketDetailView

urlpatterns = [
    path('create_ticket/', TicketCreateView.as_view(), name='create_ticket'),
    path('ticket/', TicketListView.as_view(), name='all_tickets'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket_by_id'),
]
