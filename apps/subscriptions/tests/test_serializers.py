from django.test import TestCase
from django.utils import timezone

from apps.subscriptions.serializers import SubscriptionSerializer
from apps.users.models import User
from apps.packages.models import Package


class SubscriptionSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.package = Package.objects.create(name='Test Package', price=10.0)

    def test_serializer_valid_data(self):
        data = {
            'user': self.user.id,
            'package': self.package.id,
        }
        serializer = SubscriptionSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(dict(serializer.data), data)

    def test_serializer_missing_required_field(self):
        data = {
            'user': self.user.id,
            'order_date': timezone.now().isoformat(),
        }
        serializer = SubscriptionSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('package', serializer.errors)

    def test_serializer_invalid_user_field(self):
        data = {
            'user': 999,
            'package': self.package.id,
            'order_date': timezone.now().isoformat(),
        }
        serializer = SubscriptionSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('user', serializer.errors)

    def test_serializer_invalid_package_field(self):
        data = {
            'user': self.user.id,
            'package': 999,
            'order_date': timezone.now().isoformat(),
        }
        serializer = SubscriptionSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('package', serializer.errors)

