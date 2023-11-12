from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.subscriptions.views import UserSubscriptionListView, SubscriptionView


class SubscriptionUrlsTest(SimpleTestCase):
    def test_subscribe_url_resolves(self):
        url = reverse('api:subscriptions:subscribe')
        self.assertEqual(resolve(url).func.view_class, SubscriptionView)

    def test_user_subscriptions_url_resolves(self):
        url = reverse('api:subscriptions:user-subscriptions')
        self.assertEqual(resolve(url).func.view_class, UserSubscriptionListView)
