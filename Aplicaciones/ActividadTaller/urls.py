from django.urls import path
from . import views

urlpatterns = [
    path('talleres/', views.listaTalleres, name='lista_talleres'),
    path('talleres/nuevo/', views.nuevoTaller, name='nuevo_taller'),
    path('talleres/guardar/', views.guardarTaller, name='guardar_taller'),
    path('talleres/editar/<int:id>/', views.editarTaller, name='editar_taller'),
    path('talleres/procesar/', views.procesarEdicionTaller, name='procesar_taller'),
    path('talleres/eliminar/<int:id>/', views.eliminarTaller, name='eliminar_taller'),
]
