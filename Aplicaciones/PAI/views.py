from django.shortcuts import render


from django.shortcuts import render, redirect, get_object_or_404
from .models import PAI
from Aplicaciones.Estudiantes.models import Estudiante
from django.contrib import messages

# Lista
def listaPais(request):
    pais = PAI.objects.all()
    return render(request, 'pais/inicio.html', {'pais': pais})

# Formulario nuevo
def nuevoPAI(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'pais/nuevo.html', {'estudiantes': estudiantes})

# Guardar
def guardarPAI(request):
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante_id')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        objetivos = request.POST.get('objetivos')
        acciones = request.POST.get('acciones')

        PAI.objects.create(
            estudiante_id=estudiante_id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            objetivos=objetivos,
            acciones=acciones
        )
        messages.success(request, "PAI registrado correctamente.")
        return redirect('/pais/')
    return redirect('/pais/nuevo/')

# Eliminar
def eliminarPAI(request, id):
    pai = get_object_or_404(PAI, id=id)
    pai.delete()
    messages.success(request, "PAI eliminado correctamente.")
    return redirect('/pais/')

# Editar
def editarPAI(request, id):
    pai = get_object_or_404(PAI, id=id)
    estudiantes = Estudiante.objects.all()
    return render(request, 'pais/editar.html', {
        'pai': pai,
        'estudiantes': estudiantes
    })

# Procesar edición
def procesarEdicionPAI(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pai = get_object_or_404(PAI, id=id)

        pai.estudiante_id = request.POST.get('estudiante_id')
        pai.fecha_inicio = request.POST.get('fecha_inicio')
        pai.fecha_fin = request.POST.get('fecha_fin')
        pai.objetivos = request.POST.get('objetivos')
        pai.acciones = request.POST.get('acciones')
        pai.save()

        messages.success(request, "PAI editado correctamente.")
        return redirect('/pais/')
    return redirect('/pais/')
