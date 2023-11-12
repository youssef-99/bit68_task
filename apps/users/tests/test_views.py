from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class UserRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        self.url = reverse('api:users:user-register')

    def test_user_registration(self):
        response = self.client.post(self.url, data=self.registration_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user_id', response.data)
        self.assertIn('username', response.data)
        self.assertIn('email', response.data)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_user_registration_invalid_data(self):
        invalid_data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.url, data=invalid_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)


class UserProfileViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.url = reverse('api:users:user-profile')

    def test_user_profile_retrieval(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)
