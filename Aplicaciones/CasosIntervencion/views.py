from django.shortcuts import render, redirect, get_object_or_404
from .models import CasoIntervencion , Estudiante
from django.contrib import messages

# Listar casos
def listaCasos(request):
    casos = CasoIntervencion.objects.select_related('estudiante').all()
    return render(request, 'casos/inicio.html', {'casos': casos})

# Mostrar formulario nuevo caso
def nuevoCaso(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'casos/nuevo.html', {'estudiantes': estudiantes})

# Guardar caso
def guardarCaso(request):
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante_id')
        fecha_apertura = request.POST.get('fecha_apertura')
        estado = request.POST.get('estado')
        motivo = request.POST.get('motivo')
        descripcion = request.POST.get('descripcion')

        CasoIntervencion.objects.create(
            estudiante_id=estudiante_id,
            fecha_apertura=fecha_apertura,
            estado=estado,
            motivo=motivo,
            descripcion=descripcion
        )

        messages.success(request, "Caso registrado correctamente.")
        return redirect('/casos/')
    else:
        return redirect('/casos/nuevo/')

# Eliminar caso
def eliminarCaso(request, id):
    caso = get_object_or_404(CasoIntervencion, id=id)
    caso.delete()
    messages.success(request, "Caso eliminado correctamente.")
    return redirect('/casos/')

# Formulario editar caso
def editarCaso(request, id):
    caso = get_object_or_404(CasoIntervencion, id=id)
    estudiantes = Estudiante.objects.all()
    return render(request, 'casos/editar.html', {
        'caso': caso,
        'estudiantes': estudiantes
    })
    

# Procesar edición
def procesarEdicionCaso(request, id):
    id = request.POST.get('id')
    estudiante_id = request.POST.get('estudiante_id')
    fecha_apertura = request.POST.get('fecha_apertura')
    estado = request.POST.get('estado')
    motivo = request.POST.get('motivo')
    descripcion = request.POST.get('descripcion')

    caso = CasoIntervencion.objects.get(id=id)
    caso.estudiante_id = estudiante_id
    caso.fecha_apertura = fecha_apertura
    caso.estado = estado
    caso.motivo = motivo
    caso.descripcion = descripcion

    caso.save()
    messages.success(request, "Caso editado correctamente.")
    return redirect('/casos/')
