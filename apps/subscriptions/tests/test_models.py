from django.test import TestCase
from django.utils import timezone

from apps.subscriptions.models import Subscription
from apps.users.models import User
from apps.packages.models import Package


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        self.package = Package.objects.create(name='Test Package', price=10.0)

    def test_subscription_creation(self):
        subscription = Subscription.objects.create(user=self.user, package=self.package)

        self.assertIsInstance(subscription, Subscription)
        self.assertEqual(subscription.user, self.user)
        self.assertEqual(subscription.package, self.package)
        self.assertIsNotNone(subscription.order_date)

    def test_subscription_str_method(self):
        subscription = Subscription.objects.create(user=self.user, package=self.package)
        expected_str = f"{self.user.username} subscribed to {self.package.name} on {subscription.order_date}"

        self.assertEqual(str(subscription), expected_str)

    def test_subscription_order_date_auto_now_add(self):
        before_creation = timezone.now()
        subscription = Subscription.objects.create(user=self.user, package=self.package)
        after_creation = timezone.now()

        self.assertGreaterEqual(subscription.order_date, before_creation)
        self.assertLessEqual(subscription.order_date, after_creation)

    def test_subscription_user_foreign_key(self):
        subscription = Subscription.objects.create(user=self.user, package=self.package)

        self.assertEqual(subscription.user, self.user)

    def test_subscription_package_foreign_key(self):
        subscription = Subscription.objects.create(user=self.user, package=self.package)

        self.assertEqual(subscription.package, self.package)

    def test_subscription_order_date_auto_now_add_type(self):
        subscription = Subscription.objects.create(user=self.user, package=self.package)

        self.assertIsInstance(subscription.order_date, timezone.datetime)

    def test_subscription_str_method_type(self):
        subscription = Subscription.objects.create(user=self.user, package=self.package)

        self.assertIsInstance(str(subscription), str)
