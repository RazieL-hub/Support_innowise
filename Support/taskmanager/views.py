from django.shortcuts import render
from taskmanager.models import Ticket
from taskmanager.serializers import TicketCreateSerializer
from rest_framework.views import APIView, Response
from rest_framework import generics


class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketCreateSerializer
