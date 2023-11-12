from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api'

urlpatterns = [
    path('users/', include('apps.users.urls', namespace='users')),
    path('packages/', include('apps.packages.urls', namespace='packages')),
    path('subscriptions/', include('apps.subscriptions.urls', namespace='subscriptions')),
]
