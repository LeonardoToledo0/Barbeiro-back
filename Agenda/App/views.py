from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente, Reserva, Galeria, Banner
from .serializers import (
    ClienteSerializer,
    ReservaSerializer,
    GaleriaSerializer,
    BannerSerializer
)

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Cliente views
class ClienteListView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Reserva views
class ReservaListView(ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

# Galeria views
class GaleriaListView(ListCreateAPIView):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class GaleriaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

# Banner views
class BannerListView(ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer