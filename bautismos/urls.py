from django.urls import path
from . import views


urlpatterns = [
    path('BautismoPartidas/', views.bautismopartida, name="BautismoPartidas"),
    path('pais/', views.paisform, name="paisform"),
    path('lista-paises', views.lista_paises, name='lista_paises'),
    path('editar/<int:pk>/', views.editar_pais, name='editar_pais'),
    path('eliminar/<int:pk>/', views.eliminar_pais, name='eliminar_pais'),
    path('menu/', views.menu_principal, name='menuPartidas'),
    path('login/', views.login, name='login'),
]