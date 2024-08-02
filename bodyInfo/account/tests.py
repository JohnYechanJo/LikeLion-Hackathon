# tests.py
from django.test import TestCase
from rest_framework.test import APIClient  # DRF의 APIClient 사용
from rest_framework import status
from .models import Profile
from django.contrib.auth.models import User

class ProfileTests(TestCase):
    def setUp(self):
        self.client = APIClient()  # DRF의 APIClient 사용
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.valid_payload = {
            'nickname': 'Test Nickname',
            'age': 25,
            'email': 'test@example.com',
            'phone_number': '01012345678',
            'gender': 'male',
            'height': 175.5,
            'weight': 70.5,
            'exercise_frequency': 'weekly'
        }
        self.invalid_payload = {
            'nickname': '',
            'age': 25,
            'email': 'test@example.com',
            'phone_number': '01012345678',
            'gender': 'male',
            'height': 175.5,
            'weight': 70.5,
            'exercise_frequency': 'weekly'
        }

    def test_create_valid_profile(self):
        response = self.client.post(
            '/profiles/',
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_profile(self):
        response = self.client.post(
            '/profiles/',
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)