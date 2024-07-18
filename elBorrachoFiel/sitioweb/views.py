#from .models import Nombre_Modelo de Model.py
from django.shortcuts import render

def inicio(request):
    return render(request,"index.html")
def nosotros(request):
    return render(request,"about.html")
def cerbeza(request):
    return render(request,"skills.html")
def contactos(request):
    return render(request,"proyectos.html")
def carrito(request):
    return render(request,"carrito.html")
def iniciarSesion(request):
    return render(request,"contactos.html")
def registro(request):
    return render(request,"contactos.html")

#EJEMPLO RENDERIZAR UNA DICCIONARIO EN UNA LISTA
# def usuariosVista(request):
#     listarUsuarios = Usuarios.objects.all()
#     return render(request,'plantilla.html',{'Usuarios':listarUsuarios})

