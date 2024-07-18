from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, correo, nombre, contrasena=None):
        if not correo:
            raise ValueError('Los usuarios deben tener un correo electrónico')

        user = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
        )
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre, contrasena):
        user = self.create_user(
            correo=self.normalize_email(correo),
            nombre=nombre,
            contrasena=contrasena,
        )
        user.es_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()
    verificado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    es_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.es_admin


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Nuevo campo de imagen

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADO_OPCIONES = [
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='procesando')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.TextField()
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.correo}'


class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
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


#EJEMPLO DE UNA CLASE DE LA BASE DE DATOS 
# class Usuarios(models.Model):
#     nombre = models.CharField(max_length=200)
#     correo = models.CharField(max_length=200)
#     telefono =models.CharField(max_length=200)
#     direccion = models.TextField()

        #CREANDO MI RETORNO DE LA BASE DE DATOS
#     def __str__(self):
#         return self.nombre