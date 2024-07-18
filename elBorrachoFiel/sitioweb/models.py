from django.contrib import admin

#para registrar mi base de datos en el administrador
#from .models import Usuarios<-- cambiar por tabla de la base de datos 
#admin.site.register(Usuarios)

#EJEMPLO DE UNA CLASE DE LA BASE DE DATOS 
# class Usuarios(models.Model):
#     nombre = models.CharField(max_length=200)
#     correo = models.CharField(max_length=200)
#     telefono =models.CharField(max_length=200)
#     direccion = models.TextField()

        #CREANDO MI RETORNO DE LA BASE DE DATOS
#     def __str__(self):
#         return self.nombre