from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Representante, Estudiante
from django.core.mail import EmailMessage
from django.conf import settings
import mimetypes


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

# Mostrar formulario para editar representante
def editarRepresentante(request, id):
    representante = Representante.objects.get(id=id)
    estudiantes = Estudiante.objects.all()
    return render(request, "representante/editar.html", {
        "representante": representante,
        "estudiantes": estudiantes
    })

# Procesar edición de representante
def procesarEdicionRepresentante(request, id):
    id = request.POST.get("id")
    estudiante_id = request.POST.get("estudiante_id")
    nombres = request.POST.get("nombres")
    apellidos = request.POST.get("apellidos")
    parentesco = request.POST.get("parentesco")
    telefono = request.POST.get("telefono")
    correo = request.POST.get("correo")

    representante = Representante.objects.get(id=id)
    representante.estudiante_id = estudiante_id
    representante.nombres = nombres
    representante.apellidos = apellidos
    representante.parentesco = parentesco
    representante.telefono = telefono
    representante.correo = correo

    representante.save()
    messages.success(request, "Representante EDITADO correctamente.")
    return redirect('/representante/')


# Enviar correo al representante

def enviar_representante(request, id):
    representante = get_object_or_404(Representante, id=id)

    if request.method == "POST":
        asunto = request.POST.get("asunto")
        mensaje = request.POST.get("mensaje")
        archivo = request.FILES.get("archivo")

        email = EmailMessage(
            subject=asunto,
            body=mensaje,
            from_email=settings.EMAIL_HOST_USER,
            to=[representante.correo],
        )

        if archivo:
            tipo_archivo, _ = mimetypes.guess_type(archivo.name)
            email.attach(archivo.name, archivo.read(), tipo_archivo)

        email.send(fail_silently=False)
        messages.success(request, "Correo ENVIADO exitosamente.")
        return redirect('lista_representantes')

    return render(request, 'representante/enviar.html', {
        'representante': representante
    })