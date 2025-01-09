from django.urls import path

from network.apps import NetworkConfig
from network.views import NetworkListCreateAPIView, NetworkRetrieveUpdateDestroyAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('', NetworkListCreateAPIView.as_view(), name='network-list-create'),
    path('<int:pk>/', NetworkRetrieveUpdateDestroyAPIView.as_view(), name='network-detail'),
]
