from django.urls import path
from .views import lista_direccion, lista_venta

urlpatterns = [
    path('lista_direccion', lista_direccion, name="lista_direccion"),
    path('lista_venta', lista_venta, name="lista_venta"),
]







