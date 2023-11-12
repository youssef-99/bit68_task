from django.test import TestCase

from apps.packages.models import Package


class PackageModelTest(TestCase):
    def test_package_creation(self):
        package = Package.objects.create(name='Test Package', price=10.0)

        self.assertIsInstance(package, Package)
        self.assertEqual(package.name, 'Test Package')
        self.assertEqual(package.price, 10.0)

    def test_package_str_method(self):
        package = Package.objects.create(name='Test Package', price=10.0)

        self.assertEqual(str(package), 'Test Package')
