from django.urls import path
from .views import ClienteList, ClienteDetail, ReservaList, ReservaDetail, GaleriaList, GaleriaDetail, BannerList, BannerDetail

urlpatterns = [
    path('clientes/', ClienteList.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    path('reservas/', ReservaList.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', ReservaDetail.as_view(), name='reserva-detail'),
    path('galerias/', GaleriaList.as_view(), name='galeria-list'),
    path('galerias/<int:pk>/', GaleriaDetail.as_view(), name='galeria-detail'),
    path('banners/', BannerList.as_view(), name='banner-list'),
    path('banners/<int:pk>/', BannerDetail.as_view(), name='banner-detail'),
]