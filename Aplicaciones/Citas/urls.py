from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaCitas, name='lista_citas'),
    path('nueva/', views.nuevaCita, name='nueva_cita'),
    path('guardar/', views.guardarCita, name='guardar_cita'),
    path('<int:id>/eliminar/', views.eliminarCita, name='eliminar_cita'),
    path('<int:id>/editar/', views.editarCita, name='editar_cita'),
    path('<int:id>/procesar/', views.procesarEdicionCita, name='procesar_edicion_cita'),
]