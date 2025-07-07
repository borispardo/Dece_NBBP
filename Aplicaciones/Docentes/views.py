from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente
from django.contrib import messages

# Listar docentes
def listaDocentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docente/inicio.html', {'docentes': docentes})

# Mostrar formulario para nuevo docente
def nuevoDocente(request):
    return render(request, 'docente/nuevo.html')

# Guardar docente
def guardarDocente(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        materia = request.POST.get('materia')
        correo = request.POST.get('correo')

        Docente.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            materia=materia,
            correo=correo           
        )

        messages.success(request, "Docente guardado correctamente.")
        return redirect('/docentes/')

# Eliminar docente
def eliminarDocente(request, id):
    docente = get_object_or_404(Docente, id=id)
    docente.delete()
    messages.success(request, "Docente eliminado correctamente.")
    return redirect('/docentes/')

# Mostrar formulario para editar docente
def editarDocente(request, id):
    docente = get_object_or_404(Docente, id=id)
    return render(request, 'docente/editar.html', {'docente': docente})

# Procesar edición de docente
def procesarEdicionDocente(request):

    id = request.POST.get("id")
    nombres = request.POST.get("nombres")
    apellidos = request.POST.get("apellidos")
    materia = request.POST.get("materia")
    correo = request.POST.get("correo")

    docente = Docente.objects.get(id=id)
    docente.nombres = nombres
    docente.apellidos = apellidos
    docente.materia = materia
    docente.correo = correo

    docente.save()
    messages.success(request, "Docente editado correctamente.")
    return redirect('/docentes/')



