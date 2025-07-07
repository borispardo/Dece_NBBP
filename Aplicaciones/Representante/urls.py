from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaRepresentantes, name='lista_representantes'),
    path('nuevo/', views.nuevoRepresentante, name='nuevo_representante'),
    path('guardar/', views.guardarRepresentante, name='guardar_representante'),
    path('<int:id>/eliminar/', views.eliminarRepresentante, name='eliminar_representante'),
    path('<int:id>/editar/', views.editarRepresentante, name='editar_representante'),
    path('<int:id>/actualizar/', views.procesarEdicionRepresentante, name='procesar_edicion_representante'),
]
