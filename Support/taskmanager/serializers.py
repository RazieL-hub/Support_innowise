from rest_framework import serializers
from taskmanager.models import Ticket, Comments
from authentication.models import User


class TicketCreateSerializer(serializers.ModelSerializer):
    # comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketListSerializer(serializers.ModelSerializer):
    """Список тикетов"""
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='subcategory', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    responsible = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Ticket
        fields = ('author', 'responsible', 'ticket_status', 'category', 'subcategory')


class TicketDetailSerializer(serializers.ModelSerializer):
    """Полный тикет"""
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='subcategory', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    responsible = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
