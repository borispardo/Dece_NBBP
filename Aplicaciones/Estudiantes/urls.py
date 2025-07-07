from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaEstudiantes, name='lista_estudiantes'),
    path('nuevo/', views.nuevoEstudiante, name='nuevo_estudiante'),
    path('guardar/', views.guardarEstudiante, name='guardar_estudiante'),
    path('<int:id>/eliminar/', views.eliminarEstudiante, name='eliminar_estudiante'),
    path('<int:id>/editar/', views.editarEstudiante, name='editar_estudiante'),
    path('<int:id>/actualizar/', views.procesarEdicionEstudiante, name='procesar_edicion_estudiante'),
]
