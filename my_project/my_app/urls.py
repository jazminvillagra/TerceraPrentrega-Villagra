from django.urls import path
from . import views

urlpatterns = [
    path('agregar-datos/', views.agregar_datos, name='agregar_datos'),
    path('buscar-libros/', views.buscar_libros, name='buscar_libros'),
]
