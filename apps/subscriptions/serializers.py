from rest_framework import serializers
from rest_framework.authtoken.admin import User

from apps.packages.models import Package
from apps.subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'package', 'order_date']
        read_only_fields = ['id', 'order_date']

    def validate_user(self, value):
        try:
            user = User.objects.get(pk=value.id)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid user ID')
        return user

    def validate_package(self, value):
        try:
            package = Package.objects.get(pk=value.id)
        except Package.DoesNotExist:
            raise serializers.ValidationError('Invalid package ID')
        return package
