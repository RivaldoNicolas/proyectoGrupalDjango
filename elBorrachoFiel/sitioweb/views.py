from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from .models import Cliente
from django.contrib import messages
from .models import Carrito, Pedido, DetallePedido

from .models import Producto
# from django.contrib.auth.decorators import de
# Create your views here.

def inicio(request):
    return render(request,"index.html")
def nosotros(request):
    return render(request,"nosotros.html")

def productos(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))

        producto = Producto.objects.get(id=producto_id)

        # Añadir producto al carrito
        carrito_item, created = Carrito.objects.get_or_create(
            usuario=request.user,
            producto=producto,
            defaults={'cantidad': cantidad}
        )

        if not created:
            # Si el ítem ya está en el carrito, actualizar la cantidad
            carrito_item.cantidad += cantidad
            carrito_item.save()

        return redirect('carrito')  # Asegúrate de que la URL 'carrito' esté configurada

    listarProducto = Producto.objects.all()
    return render(request, "productos.html", {'productos': listarProducto})
def contactos(request):
    return render(request,"contactos.html")

def carrito(request):
    usuario = request.user

    # Obtenemos los elementos del carrito del usuario
    carrito_items = Carrito.objects.filter(usuario=usuario)
    
    # Creamos una lista para almacenar los elementos del carrito junto con el total por item
    carrito_con_totales = []
    total_carrito = 0

    for item in carrito_items:
        total_item = item.producto.precio * item.cantidad
        total_carrito += total_item
        carrito_con_totales.append({
            'item': item,
            'total_item': total_item
        })
    
    if request.method == 'POST':
        direccion_envio = request.POST.get('direccion_envio')
        metodo_pago = request.POST.get('metodo_pago')
        
        # Verificamos que los campos obligatorios estén presentes
        if not direccion_envio or not metodo_pago:
            messages.error(request, 'Por favor, complete todos los campos.')
            return redirect('carrito')  # Asegúrate de que la URL 'carrito' esté configurada

        # Creamos el pedido
        pedido = Pedido.objects.create(
            usuario=usuario,
            total=total_carrito,
            direccion_envio=direccion_envio,
            metodo_pago=metodo_pago
        )

        # Creamos los detalles del pedido
        for item in carrito_items:
            DetallePedido.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.producto.precio
            )
        
        # Eliminamos los elementos del carrito después de crear el pedido
        carrito_items.delete()
        
        messages.success(request, 'Compra realizada con éxito.')
        return redirect('inicio')  # Asegúrate de que la URL 'inicio' esté configurada

    context = {
        'carrito': carrito_con_totales,
        'total': total_carrito,
    }

    return render(request, 'carrito.html', context)
def dashword(request):
    return render(request,'dashword.html')

def vistaLogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuarios = authenticate(request,username=username,password=password)
        if usuarios is not None:
            login(request,usuarios)
            return redirect('cuentaCliente')
        else:
            return redirect('login',{'error':'datos incorrectos'})
    return render(request,"login.html")

def crearUsuario(request):
    if request.method == "POST":
        formUsuario = request.POST.get("nuevoCliente")
        formPassword = request.POST.get("nuevaClave")
        insertarCliente= User.objects.create_user(username=formUsuario,password=formPassword)
        if insertarCliente is not None:
            login( request,insertarCliente)
            return redirect("cuentaCliente")
    return render(request,"registrar.html")

def salirUsuario(request):
    logout(request)
    return render(request,"index.html")

def cuentaCliente(request):
   return render(request, 'dashboard.html')


from django.contrib.auth.decorators import login_required


@login_required
def registrarCliente(request):
    if request.method == "POST":
        formDni = request.POST.get('dni')
        formTelefono = request.POST.get('telefono')
        formFechaNacimiento = request.POST.get('fecha_nacimiento')
        formDireccion = request.POST.get('direccion')

        # Crear un nuevo registro de Cliente
        insertarRegistro = Cliente(
            usuario=request.user,
            dni=formDni,
            telefono=formTelefono,
            fecha_nacimiento=formFechaNacimiento,
            direccion=formDireccion
        )
        insertarRegistro.save()
        return redirect('cuentaCliente')  # Asegúrate de tener definida esta URL

    return render(request, "cliente.html")
