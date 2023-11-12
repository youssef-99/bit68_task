from django.test import TestCase

from apps.packages.models import Package
from apps.packages.serializers import PackageSerializer


class PackageSerializerTest(TestCase):
    def setUp(self):
        self.package_data = {'name': 'Test Package', 'price': 10.0}

    def test_serializer_valid_data(self):
        serializer = PackageSerializer(data=self.package_data)

        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.validated_data, self.package_data)

    def test_serializer_missing_required_field(self):
        data = {'name': 'Test Package'}
        serializer = PackageSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)

    def test_serializer_invalid_price_field(self):
        data = {'name': 'Test Package', 'price': 'invalid'}
        serializer = PackageSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)

    def test_serializer_read_only_fields(self):
        package = Package.objects.create(name='Test Package', price=10.0)
        serializer = PackageSerializer(instance=package)

        expected_data = {'id': package.id, 'name': 'Test Package', 'price': '10.00'}

        self.assertEqual(serializer.data, expected_data)
