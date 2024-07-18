from django.contrib import admin

#para registrar mi base de datos en el administrador
from .models import Producto, Pedido,Usuario,DetallePedido,Carrito
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(DetallePedido)

# Register your models here.
