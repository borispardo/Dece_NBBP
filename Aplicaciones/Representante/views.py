from django.shortcuts import render, redirect, get_object_or_404
from .models import Representante, Estudiante
from django.contrib import messages

# Listar representantes
def listaRepresentantes(request):
    representantes = Representante.objects.select_related('estudiante').all()
    return render(request, 'representante/inicio.html', {'representantes': representantes})

# Mostrar formulario para nuevo representante
def nuevoRepresentante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'representante/nuevo.html', {'estudiantes': estudiantes})

# Guardar representante
def guardarRepresentante(request):
    if request.method == "POST":
        estudiante_id = request.POST.get("estudiante_id")
        nombres = request.POST.get("nombres")
        apellidos = request.POST.get("apellidos")
        parentesco = request.POST.get("parentesco")
        telefono = request.POST.get("telefono")
        correo = request.POST.get("correo")

        Representante.objects.create(
            estudiante_id=estudiante_id,
            nombres=nombres,
            apellidos=apellidos,
            parentesco=parentesco,
            telefono=telefono,
            correo=correo
        )

        messages.success(request, "Representante GUARDADO correctamente.")
        return redirect('/representante/')
    else:
        return redirect('/representante/nuevo/')

# Eliminar representante
def eliminarRepresentante(request, id):
    representante = Representante.objects.get(id=id)
    representante.delete()
    messages.success(request, "Representante ELIMINADO correctamente.")
    return redirect('/representante/')


