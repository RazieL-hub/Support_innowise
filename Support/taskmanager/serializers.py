from rest_framework import serializers
from taskmanager.models import Ticket, Comments


class TicketCreateSerializer(serializers.ModelSerializer):
    #comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ticket
        fields = '__all__'
