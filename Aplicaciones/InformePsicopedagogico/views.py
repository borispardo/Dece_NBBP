from django.shortcuts import render, redirect, get_object_or_404
from .models import InformePsicopedagogico
from Aplicaciones.Estudiantes.models import Estudiante
from django.contrib import messages

# Listar informes
def listaInformes(request):
    informes = InformePsicopedagogico.objects.all()
    return render(request, 'informes/inicio.html', {'informes': informes})

# Mostrar formulario nuevo informe
def nuevoInforme(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'informes/nuevo.html', {'estudiantes': estudiantes})

# Guardar informe
def guardarInforme(request):
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        fecha = request.POST.get('fecha')
        contenido = request.POST.get('contenido')
        recomendaciones = request.POST.get('recomendaciones')

        InformePsicopedagogico.objects.create(
            estudiante_id=estudiante_id,
            fecha=fecha,
            contenido=contenido,
            recomendaciones=recomendaciones
        )

        messages.success(request, "Informe registrado correctamente.")
        return redirect('/informes/')
    else:
        return redirect('/informes/nuevo/')

# Eliminar informe
def eliminarInforme(request, id):
    informe = get_object_or_404(InformePsicopedagogico, id=id)
    informe.delete()
    messages.success(request, "Informe eliminado correctamente.")
    return redirect('/informes/')

# Formulario editar informe
def editarInforme(request, id):
    informe = get_object_or_404(InformePsicopedagogico, id=id)
    estudiantes = Estudiante.objects.all()
    return render(request, 'informes/editar.html', {'informe': informe, 'estudiantes': estudiantes})

# Procesar edición
def procesarEdicionInforme(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        informe = get_object_or_404(InformePsicopedagogico, id=id)

        informe.estudiante_id = request.POST.get('estudiante_id')
        informe.fecha = request.POST.get('fecha')
        informe.contenido = request.POST.get('contenido')
        informe.recomendaciones = request.POST.get('recomendaciones')

        informe.save()
        messages.success(request, "Informe editado correctamente.")
        return redirect('/informes/')
    else:
        return redirect('/informes/')