from rest_framework import serializers
from authentication.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class RegisterSerializer(serializers.ModelSerializer):
    # username = serializers.RegexField(regex=r'[0-9a-zA-Z-_]', max_length=54, allow_blank=False,
    #                                   error_messages={'invalid': 'username содержит недопустимые символы'})
    # password = serializers.CharField(max_length=54, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=54, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password')
        errors = dict()

        if password != confirm_password:
            raise serializers.ValidationError('Password и Password2 не совпадают!!!')
        try:
            validators.validate_password(password=password)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        attrs.pop('confirm_password', None)
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
