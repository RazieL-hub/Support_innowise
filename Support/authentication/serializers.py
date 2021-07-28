from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=54, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError("Имя пользователя должно состоять только из букв и цифр. "
                                              "Мнимальное количество букв - 1")
        return attrs

    def create(self, validated_data):
        return User.objects.create(**validated_data)
