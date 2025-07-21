from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password

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
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        rol = request.POST.get('rol')
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')

        if id:  # editar
            usuario = get_object_or_404(Usuario, id=id)
            usuario.nombre = nombre
            usuario.rol = rol
            usuario.correo = correo
            if clave:
                usuario.clave = make_password(clave)
            usuario.save()
            messages.success(request, 'Usuario actualizado correctamente.')
        else:  # nuevo
            Usuario.objects.create(
                nombre=nombre,
                rol=rol,
                correo=correo,
                clave=make_password(clave)
            )
            messages.success(request, 'Usuario creado correctamente.')

        return redirect('/usuarios/')

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

def loginUsuario(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        clave = request.POST.get("clave")
        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(clave, usuario.clave):
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                request.session['usuario_rol'] = usuario.rol
                messages.success(request, "Bienvenido " + usuario.nombre)
                return redirect('dashboard')
            else:
                messages.error(request, "Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            messages.error(request, "El correo no existe.")

    return render(request, "usuarios/login.html")

def dashboard(request):
    rol = request.session.get('usuario_rol')
    nombre = request.session.get('usuario_nombre')

    if not rol:
        return redirect('login')  # si no hay sesión, redirige al login

    return render(request, 'usuarios/dashboard.html', {'rol': rol, 'nombre': nombre})

def logoutUsuario(request):
    request.session.flush()
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('login')

