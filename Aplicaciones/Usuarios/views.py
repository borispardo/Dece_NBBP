from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Lista
def listaUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/inicio.html', {'usuarios': usuarios})

# Nuevo
def nuevoUsuario(request):
    return render(request, 'usuarios/nuevo.html')

# Guardar
def guardarUsuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rol = request.POST.get('rol')
        correo = request.POST.get('correo')
        clave = make_password(request.POST.get('clave'))

        Usuario.objects.create(nombre=nombre, rol=rol, correo=correo, clave=clave)
        messages.success(request, "Usuario registrado correctamente.")
        return redirect('/usuarios/')
    return redirect('/usuarios/nuevo/')

# Eliminar
def eliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, "Usuario eliminado.")
    return redirect('/usuarios/')

# Editar
def editarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'usuarios/editar.html', {'usuario': usuario})

# Procesar edición
def procesarEdicionUsuario(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        usuario = get_object_or_404(Usuario, id=id)

        usuario.nombre = request.POST.get('nombre')
        usuario.rol = request.POST.get('rol')
        usuario.correo = request.POST.get('correo')
        nueva_clave = request.POST.get('clave')

        if nueva_clave:
            usuario.clave = make_password(nueva_clave)

        usuario.save()
        messages.success(request, "Usuario editado correctamente.")
        return redirect('/usuarios/')
    return redirect('/usuarios/')