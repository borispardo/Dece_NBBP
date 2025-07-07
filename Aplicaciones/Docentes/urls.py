from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaDocentes, name='lista_docentes'),
    path('nuevo/', views.nuevoDocente, name='nuevo_docente'),
    path('guardar/', views.guardarDocente, name='guardar_docente'),
    path('<int:id>/eliminar/', views.eliminarDocente, name='eliminar_docente'),
    path('<int:id>/editar/', views.editarDocente, name='editar_docente'),
    path('<int:id>/actualizar/', views.procesarEdicionDocente, name='procesar_edicion_docente'),
]
