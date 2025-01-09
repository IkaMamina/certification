from django.shortcuts import render
from rest_framework import generics

from network.models import Network
from network.serializers import NetworkSerializer


class NetworkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NetworkRetrieveUpdateDestroyAPIView(generics.ListCreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

