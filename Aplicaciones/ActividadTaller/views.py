from django.shortcuts import render, redirect, get_object_or_404
from .models import ActividadTaller
from django.contrib import messages

# Listar todas las actividades
def listaTalleres(request):
    talleres = ActividadTaller.objects.all()
    return render(request, 'taller/inicio.html', {'talleres': talleres})

# Mostrar formulario para crear nueva actividad
def nuevoTaller(request):
    return render(request, 'taller/nuevo.html')

# Guardar actividad
def guardarTaller(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        fecha = request.POST.get("fecha")
        descripcion = request.POST.get("descripcion")

        ActividadTaller.objects.create(
            nombre=nombre,
            fecha=fecha,
            descripcion=descripcion
        )

        messages.success(request, "Taller GUARDADO correctamente.")
        return redirect('/talleres/')
    else:
        return redirect('/talleres/nuevo/')

# Mostrar formulario para editar
def editarTaller(request, id):
    taller = get_object_or_404(ActividadTaller, id=id)
    return render(request, 'taller/editar.html', {"taller": taller})

# Procesar edición
def procesarEdicionTaller(request, id):
    taller = get_object_or_404(ActividadTaller, id=id)

    if request.method == "POST":
        taller.nombre = request.POST.get("nombre")
        taller.fecha = request.POST.get("fecha")
        taller.descripcion = request.POST.get("descripcion")
        taller.save()
        messages.success(request, "Taller EDITADO correctamente.")
        return redirect('/talleres/')
    else:
        # Si alguien accede con GET, lo rediriges
        return redirect('/talleres/')

# Eliminar actividad
def eliminarTaller(request, id):
    taller = get_object_or_404(ActividadTaller, id=id)
    taller.delete()
    messages.success(request, "Taller ELIMINADO correctamente.")
    return redirect('/talleres/')
