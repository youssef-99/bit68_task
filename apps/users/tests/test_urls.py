from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserRegistrationView, UserProfileView


class UserUrlsTest(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_url_resolves(self):
        url = reverse('api:users:token_obtain_pair')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_refresh_token_url_resolves(self):
        url = reverse('api:users:token_refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_register_url_resolves(self):
        url = reverse('api:users:user-register')
        self.assertEqual(resolve(url).func.view_class, UserRegistrationView)

    def test_profile_url_resolves(self):
        url = reverse('api:users:user-profile')
        self.assertEqual(resolve(url).func.view_class, UserProfileView)

