import json

from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response

from .models import Subscription
from .serializers import SubscriptionSerializer
from ..packages.models import Package


class SubscriptionView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        package_ids = json.loads(request.data.get('packages', '[]'))

        existing_subscriptions = Subscription.objects.filter(user=self.request.user, package__id__in=package_ids)

        if existing_subscriptions.exists():
            existing_package_ids = set(subscription.package.id for subscription in existing_subscriptions)
            raise serializers.ValidationError({'error': f'User already has subscriptions with packages {existing_package_ids}'})

        packages = Package.objects.filter(pk__in=package_ids)

        if not packages.exists():
            return Response({'error': 'Invalid package IDs provided'}, status=400)

        subscriptions_to_create = [
            Subscription(user=self.request.user, package=package)
            for package in packages
        ]
        Subscription.objects.bulk_create(subscriptions_to_create)

        serializer = self.get_serializer(subscriptions_to_create, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserSubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
