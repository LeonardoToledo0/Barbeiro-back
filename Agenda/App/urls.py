from django.urls import path
from .views import (
    ClienteListView, ClienteDetailView,
    ReservaListView, ReservaDetailView,
    GaleriaListView, GaleriaDetailView,
    BannerListView, BannerDetailView
)

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('reservas/', ReservaListView.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detail'),
    path('galerias/', GaleriaListView.as_view(), name='galeria-list'),
    path('galerias/<int:pk>/', GaleriaDetailView.as_view(), name='galeria-detail'),
    path('banners/', BannerListView.as_view(), name='banner-list'),
    path('banners/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),
]