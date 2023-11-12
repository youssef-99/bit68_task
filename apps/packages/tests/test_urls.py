from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.packages.views import PackageListView


class PackageUrlsTest(SimpleTestCase):
    def test_package_list_url_resolves(self):
        url = reverse('api:packages:package-list')
        self.assertEqual(resolve(url).func.view_class, PackageListView)
