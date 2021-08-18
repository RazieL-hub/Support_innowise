from django.shortcuts import render
from taskmanager.models import Ticket
from taskmanager.serializers import TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response


class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketCreateSerializer


class TicketListView(APIView):
    """Вывод полного списка тикетов"""

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketListSerializer(tickets, many=True)
        return Response(serializer.data)


class TicketDetailView(APIView):
    """Вывод конкретного тикетов"""

    def get(self, request, pk):
        tickets = Ticket.objects.get(id=pk)
        serializer = TicketDetailSerializer(tickets)
        return Response(serializer.data)
