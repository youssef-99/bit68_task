from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from apps.packages.models import Package
from apps.users.models import User


class PackageListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.url = reverse('api:packages:package-list')

        self.package1 = Package.objects.create(name='Package 1', price=10.0)
        self.package2 = Package.objects.create(name='Package 2', price=20.0)
        self.package3 = Package.objects.create(name='Another Package', price=15.0)

    def test_package_list_view_authenticated(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_package_list_view_unauthenticated(self):
        client = APIClient()

        response = client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_package_list_view_ordering(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get(self.url, {'ordering': 'price'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['price'], '10.00')
        self.assertEqual(response.data[1]['price'], '15.00')
        self.assertEqual(response.data[2]['price'], '20.00')

    def test_package_list_view_search(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get(self.url, {'search': 'Package'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
