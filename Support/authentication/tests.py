import json

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class UsersApiTestCase(APITestCase):
    def test_user(self):
        url = "/authentication/register/"
        data = {
            "email": "test_staff@admin.com",
            "username": "test_staff",
            "password": "superuser1234",
            "confirm_password": "superuser1234",
            "is_active": 'True',
            "is_superuser": 'False',
            "is_staff": 'False',
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data['email'], response.data['email'])
        self.assertEqual(data['username'], response.data['username'])
        self.assertEqual(data['password'], response.data['password'])
        self.assertEqual(3, len(response.data))

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test_user@test.com', username='test_user', password='testuser1234',
                                        is_staff=False, is_superuser=False)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='test_superuser@test.com', username='super_user',
                                                   password='superuser', )
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
