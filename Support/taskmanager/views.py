from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from taskmanager.models import Ticket, Comment
from taskmanager.serializers import TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer, \
    CommentCreateSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response


class TicketCreateView(generics.CreateAPIView):
    """Создание тикета"""
    serializer_class = TicketCreateSerializer
    permission_classes = (AllowAny,)


class TicketListView(generics.ListAPIView):
    """Вывод полного списка тикетов"""
    serializer_class = TicketListSerializer
    permission_classes = (AllowAny, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory', 'ticket_status']


    def get_queryset(self):
        tickets = Ticket.objects.all()
        return tickets




class TicketDetailView(generics.RetrieveAPIView):
    """Вывод конкретного тикетов"""

    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.filter()

class CommentCreateView(generics.CreateAPIView):
    """Добавление комментария"""
    serializer_class = CommentCreateSerializer



class Test(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
