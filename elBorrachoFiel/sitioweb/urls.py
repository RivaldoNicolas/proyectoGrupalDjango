from django.urls import path
from . import  views 

urlpatterns = [
    path("",views.inicio, name=("inicio")),
    path("nosotros/",views.nosotros, name=("nosotros")),
    path("productos/",views.productos, name=("productos")),
    path("contactos/",views.contactos, name=("contactos")),
    path("carrito/",views.carrito, name=("carrito")),
    path("iniciarSesion/",views.iniciarSesion, name=("iniciarSesion")),
    path("registrarse/",views.registrarse, name=("registrarse")),
    path("dashword/",views.dashword, name=("panel")),
]
