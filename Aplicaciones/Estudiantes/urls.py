from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaEstudiantes, name='lista'),
    path('nuevo/', views.nuevoEstudiante, name='nuevo'),
    path('guardar/', views.guardarEstudiante, name='guardar'),
    path('<int:id>/eliminar/', views.eliminarEstudiante, name='eliminar'),
    path('<int:id>/editar/', views.editarEstudiante, name='editar'),
    path('editar/', views.procesarEdicionEstudiante, name='procesarEdicion'),

]