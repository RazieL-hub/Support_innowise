from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from taskmanager.models import Ticket
from taskmanager.serializers import TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer, \
    CommentCreateSerializer
from rest_framework import generics


class TicketCreateView(generics.CreateAPIView):
    """Создание тикета"""
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketCreateSerializer

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()


class TicketListView(generics.ListAPIView):
    """Вывод полного списка тикетов"""
    serializer_class = TicketListSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory', 'ticket_status']

    def get_queryset(self):
        tickets = Ticket.objects.all()
        return tickets


class TicketDetailView(generics.RetrieveAPIView):
    """Вывод конкретного тикетов"""

    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()


class CommentCreateView(generics.CreateAPIView):
    """Добавление комментария"""
    serializer_class = CommentCreateSerializer


class Test(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
