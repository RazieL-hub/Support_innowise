from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.models import User
from authentication.serializers import RegisterSerializer
from rest_framework import permissions
from authentication.service import send
from authentication.tasks import send_activation_email

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data     # переменная хранит данные пользовательского запроса.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        print(dir(serializer))
        print('___________________________________')
        print(serializer.validated_data)
        current_site = get_current_site(request).domain

        email_subject = 'Verify your email'
        email_body = f"Hi {serializer.validated_data.get('username')}. Use link for verify your email." \
                     f" "
        send_activation_email.delay(serializer.validated_data.get('email'))

        return Response(user_data, status=status.HTTP_201_CREATED)

