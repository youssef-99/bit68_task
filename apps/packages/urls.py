from django.urls import path
from .views import PackageListView

app_name = 'packages'

urlpatterns = [
    path('', PackageListView.as_view(), name='package-list'),
]
