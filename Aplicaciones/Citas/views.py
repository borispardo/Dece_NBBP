from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from Aplicaciones.CasosIntervencion.models import CasoIntervencion
from django.contrib import messages

# Lista de sesiones
def listaCitas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/inicio.html', {'citas': citas})

# Mostrar formulario para nueva cita
def nuevaCita(request):
    casos = CasoIntervencion.objects.all()
    return render(request, 'citas/nuevo.html', {'casos': casos})

# Guardar cita
def guardarCita(request):
    if request.method == 'POST':
        caso_id = request.POST.get('caso')
        fecha = request.POST.get('fecha')
        profesional = request.POST.get('profesional')
        observaciones = request.POST.get('observaciones')
        cita = Cita.objects.create(
            caso_id=caso_id,
            fecha=fecha,
            profesional=profesional,
            observaciones=observaciones
        )

        messages.success(request, "Cita guardada correctamente.")
        return redirect('/citas/')
    else:
        return redirect('/citas/nuevo/')

# Eliminar cita
def eliminarCita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    messages.success(request, "Cita eliminada correctamente.")
    return redirect('/citas/')

# Mostrar formulario para editar cita
def editarCita(request, id):
    cita = get_object_or_404(Cita, id=id)
    casos = CasoIntervencion.objects.all()
    return render(request, 'citas/editar.html', {'cita': cita, 'casos': casos})

# Procesar edición de cita
def procesarEdicionCita(request, id):
    if request.method == 'POST':
        caso_id = request.POST.get("caso")
        fecha = request.POST.get("fecha")
        profesional = request.POST.get("profesional")
        observaciones = request.POST.get("observaciones")

        cita = get_object_or_404(Cita, id=id)
        cita.caso_id = caso_id
        cita.fecha = fecha
        cita.profesional = profesional
        cita.observaciones = observaciones

        cita.save()
        messages.success(request, "Cita editada correctamente.")
        return redirect('/citas/')
    else:
        return redirect('/citas/')