from django.shortcuts import render
from rest_framework import generics
from .models import Cliente, Reserva, Galeria, Banner
from .serializers import ClienteSerializer, ReservaSerializer, GaleriaSerializer, BannerSerializer

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class GaleriaList(generics.ListCreateAPIView):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class GaleriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class BannerList(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer