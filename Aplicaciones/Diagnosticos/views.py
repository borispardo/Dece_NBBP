from django.shortcuts import render, redirect, get_object_or_404
from .models import Diagnostico
from Aplicaciones.Estudiantes.models import Estudiante
from django.contrib import messages

# Mostrar lista
def listaDiagnosticos(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnosticos/inicio.html', {'diagnosticos': diagnosticos})

# Nuevo formulario
def nuevoDiagnostico(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'diagnosticos/nuevo.html', {'estudiantes': estudiantes})

# Guardar
def guardarDiagnostico(request):
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante_id')
        tipo = request.POST.get('tipo')
        otro_tipo = request.POST.get('otro_tipo', '').strip()
        descripcion = request.POST.get('descripcion')

        if tipo == 'Otro' and otro_tipo:
            tipo = otro_tipo

        Diagnostico.objects.create(
            estudiante_id=estudiante_id,
            tipo=tipo,
            descripcion=descripcion
        )
        messages.success(request, "Diagnóstico registrado correctamente.")
        return redirect('/diagnosticos/')
    return redirect('/diagnosticos/nuevo/')

# Eliminar
def eliminarDiagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id=id)
    diagnostico.delete()
    messages.success(request, "Diagnóstico eliminado correctamente.")
    return redirect('/diagnosticos/')

# Editar
def editarDiagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id=id)
    estudiantes = Estudiante.objects.all()
    return render(request, 'diagnosticos/editar.html', {
        'diagnostico': diagnostico,
        'estudiantes': estudiantes
    })

# Procesar edición
def procesarEdicionDiagnostico(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        diagnostico = get_object_or_404(Diagnostico, id=id)

        tipo = request.POST.get('tipo')
        otro_tipo = request.POST.get('otro_tipo', '').strip()

        if tipo == 'Otro' and otro_tipo:
            tipo = otro_tipo

        diagnostico.estudiante_id = request.POST.get('estudiante_id')
        diagnostico.tipo = tipo
        diagnostico.descripcion = request.POST.get('descripcion')
        diagnostico.save()

        messages.success(request, "Diagnóstico editado correctamente.")
        return redirect('/diagnosticos/')
    return redirect('/diagnosticos/')
