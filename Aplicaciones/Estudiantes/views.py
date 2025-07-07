from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from django.contrib import messages

# Listar estudiantes
def listaEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/inicio.html', {'estudiantes': estudiantes})

# Mostrar formulario para nuevo estudiante
def nuevoEstudiante(request):
    return render(request, 'estudiante/nuevo.html')

# Guardar estudiante
def guardarEstudiante(request):
    if request.method == "POST":
        nombres = request.POST.get("nombres")
        apellidos = request.POST.get("apellidos")
        cedula = request.POST.get("cedula")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        genero = request.POST.get("genero")
        direccion = request.POST.get("direccion")
        telefono = request.POST.get("telefono")
        correo = request.POST.get("correo")
        curso = request.POST.get("curso")
        historial = request.POST.get("historial")

        Estudiante.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            cedula=cedula,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            curso=curso,
            historial=historial
        )

        messages.success(request, "Estudiante GUARDADO correctamente.")
        return redirect('/estudiantes/')
    else:
        return redirect('/estudiantes/nuevo/')

# Eliminar estudiante
def eliminarEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    messages.success(request, "Estudiante ELIMINADO correctamente.")
    return redirect('/estudiantes/')

# Mostrar formulario para editar estudiante
def editarEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, "estudiante/editar.html", {"estudiante": estudiante})


# Procesar edición de estudiante
def procesarEdicionEstudiante(request, id):

    id = request.POST.get("id")
    nombres = request.POST.get("nombres")
    apellidos = request.POST.get("apellidos")
    cedula = request.POST.get("cedula")
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    genero = request.POST.get("genero")
    direccion = request.POST.get("direccion")
    telefono = request.POST.get("telefono")
    correo = request.POST.get("correo")
    curso = request.POST.get("curso")
    historial = request.POST.get("historial")
    
    estudiante = Estudiante.objects.get(id=id)
    estudiante.nombres = nombres
    estudiante.apellidos = apellidos
    estudiante.cedula = cedula
    estudiante.fecha_nacimiento = fecha_nacimiento
    estudiante.genero = genero
    estudiante.direccion = direccion
    estudiante.telefono = telefono
    estudiante.correo = correo
    estudiante.curso = curso
    estudiante.historial = historial

    estudiante.save()
    messages.success(request, "Estudiante EDITADO correctamente.")
    return redirect('/estudiantes/')

