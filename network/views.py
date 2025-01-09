from django.shortcuts import render
from rest_framework import generics

from network.models import Network
from network.permissions import IsActiveUser
from network.serializers import NetworkSerializer


class NetworkListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsActiveUser]
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NetworkRetrieveUpdateDestroyAPIView(generics.ListCreateAPIView):
    permission_classes = [IsActiveUser]
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

