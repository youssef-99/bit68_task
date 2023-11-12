from rest_framework import generics, permissions
from rest_framework import filters
from .models import Package
from .serializers import PackageSerializer


class PackageListView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]

