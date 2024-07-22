from django.db import models
from django.contrib.auth.models import User

# Modelo para registrar información general
class Registro(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fecha = models.DateField()
    contenido = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para información adicional del cliente
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
    dni = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField()

    def __str__(self):
        return self.usuario.username

# Modelos para productos y pedidos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADO_OPCIONES = [
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='procesando')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.TextField()
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.username}'

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.producto.nombre} x {self.cantidad}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad}'
