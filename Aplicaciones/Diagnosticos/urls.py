from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaDiagnosticos, name='lista_diagnosticos'),
    path('nuevo/', views.nuevoDiagnostico, name='nuevo_diagnostico'),
    path('guardar/', views.guardarDiagnostico, name='guardar_diagnostico'),
    path('<int:id>/eliminar/', views.eliminarDiagnostico, name='eliminar_diagnostico'),
    path('<int:id>/editar/', views.editarDiagnostico, name='editar_diagnostico'),
    path('editar/', views.procesarEdicionDiagnostico, name='procesar_edicion_diagnostico'),
]
