from django.urls import path
from AppCafe import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    #path('pedido/', views.pedidos, name="Pedidos"),
]
