from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from django.contrib import messages

# Listar estudiantes
def listaEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})

# Mostrar formulario para nuevo estudiante
def nuevoEstudiante(request):
    return render(request, 'estudiantes/nuevo.html')

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
    estudianteEditar = Estudiante.objects.get(id=id)
    return render(request, "estudiantes/editar.html", {"estudianteEditar": estudianteEditar})

# Procesar edición de estudiante
def procesarEdicionEstudiante(request):
    if request.method == "POST":
        id = request.POST["id"]
        estudiante = Estudiante.objects.get(id=id)

        estudiante.nombres = request.POST["nombres"]
        estudiante.apellidos = request.POST["apellidos"]
        estudiante.cedula = request.POST["cedula"]
        estudiante.fecha_nacimiento = request.POST["fecha_nacimiento"]
        estudiante.genero = request.POST["genero"]
        estudiante.direccion = request.POST["direccion"]
        estudiante.telefono = request.POST["telefono"]
        estudiante.correo = request.POST["correo"]
        estudiante.curso = request.POST["curso"]
        estudiante.historial = request.POST["historial"]

        estudiante.save()
        messages.success(request, "Estudiante EDITADO correctamente.")
        return redirect('/estudiantes/')
    else:
        return redirect('/estudiantes/')
