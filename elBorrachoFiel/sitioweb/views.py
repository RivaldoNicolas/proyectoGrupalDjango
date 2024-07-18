#from .models import Nombre_Modelo de Model.py
from django.shortcuts import render

def inicio(request):
    return render(request,"index.html")
def nosotros(request):
    return render(request,"nosotros.html")
def productos(request):
    return render(request,"productos.html")
def contactos(request):
    return render(request,"contactos.html")
def carrito(request):
    return render(request,"carrito.html")
def iniciarSesion(request):
    return render(request,"iniciarSesion.html")
def registrarse(request):
    return render(request,"registrarse.html")

#EJEMPLO RENDERIZAR UNA DICCIONARIO EN UNA LISTA
# def usuariosVista(request):
#     listarUsuarios = Usuarios.objects.all()
#     return render(request,'plantilla.html',{'Usuarios':listarUsuarios})

