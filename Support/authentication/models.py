from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):  # Специальный класс для создания новых пользователей
    # Создаём метод для создания пользователя
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Вы не ввели Email')
        if not username:
            raise ValueError('Вы не ввели Username')
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)

        user.save()
        return user

    # Делаем метод для создание суперпользователя
    def create_superuser(self, email, username, password=None):
        if password is None:
            raise TypeError('Поле password не может быть пустым')
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=54, unique=True, db_index=True, validators=[RegexValidator(
            regex=r'[^0-9a-zA-Z-_]',
            message='Only use letters, numbers - and _',
            code='invalid_username',
            inverse_match=True,
        )],
                                )
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # константа - ИДЕНТИФИКАТОР ЛОГИНА
    REQUIRED_FIELDS = ['username']  # обязательные поля для ВВОДА

    objects = UserManager()

    def __str__(self):
        return f'{self.email} {self.username}'


class Profile(models.Model):
    class Gender(models.TextChoices):
        m = 'm', _('male')
        f = 'f', _('female')

    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    gender = models.CharField(max_length=32, choices=Gender.choices, default='m')
    age = models.SmallIntegerField()
    city = models.CharField(max_length=254)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
