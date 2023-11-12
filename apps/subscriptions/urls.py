from django.urls import path

from apps.subscriptions.views import SubscriptionView, UserSubscriptionListView

app_name = 'subscriptions'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('user-subscriptions/', UserSubscriptionListView.as_view(), name='user-subscriptions'),
]
