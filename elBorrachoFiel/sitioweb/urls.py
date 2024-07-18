from django.urls import path
from . import  views 

urlpatterns = [
    path("",views.inicio, name=("inicio")),
    path("nosotros/",views.nosotros, name=("nosotros")),
    path("cerbeza/",views.cerbeza, name=("cerbeza")),
    path("contactos/",views.contactos, name=("contactos")),
    path("carrito/",views.carrito, name=("carrito")),
    path("iniciarSesion/",views.iniciarSesion, name=("iniciarSesion")),
    path("registro/",views.registro, name=("registro")),
]
