from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.users.serializers import UserSerializer

User = get_user_model()


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        }

    def test_serializer_valid_data(self):
        serializer = UserSerializer(data=self.user_data)

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.validated_data, self.user_data)

    def test_serializer_missing_required_field(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        serializer = UserSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_serializer_create_user(self):
        serializer = UserSerializer(data=self.user_data)
        serializer.is_valid()
        user = serializer.save()

        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_serializer_password_write_only(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        serializer = UserSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertNotIn('password', serializer.data)
