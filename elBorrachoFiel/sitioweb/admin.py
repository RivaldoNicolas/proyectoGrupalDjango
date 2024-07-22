from django.contrib import admin

#para registrar mi base de datos en el administrador
from .models import Producto, Pedido,DetallePedido,Carrito, Cliente
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(DetallePedido)
admin.site.register(Cliente)

# Register your models here.
