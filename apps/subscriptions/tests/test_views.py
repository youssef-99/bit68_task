import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from apps.subscriptions.models import Subscription
from apps.users.models import User
from apps.packages.models import Package


class SubscriptionViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.package1 = Package.objects.create(name='Package 1', price=10.0)
        self.package2 = Package.objects.create(name='Package 2', price=20.0)
        self.url = reverse('api:subscriptions:subscribe')

    def test_subscription_creation(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        data = {'packages': json.dumps([self.package1.id, self.package2.id])}
        response = client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.filter(user=self.user).count(), 2)

    def test_subscription_existing_subscriptions(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        Subscription.objects.create(user=self.user, package=self.package1)

        data = {'packages': json.dumps([self.package1.id, self.package2.id])}
        response = client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('User already has subscriptions with packages', response.data['error'])

    def test_subscription_invalid_package_ids(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        data = {'packages': json.dumps([999, 888])}
        response = client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Invalid package IDs provided', response.data['error'])


class UserSubscriptionListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.package = Package.objects.create(name='Test Package', price=10.0)
        self.subscription = Subscription.objects.create(user=self.user, package=self.package)
        self.url = reverse('api:subscriptions:user-subscriptions')

    def test_user_subscription_list(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.id)
        self.assertEqual(response.data[0]['package'], self.package.id)
