from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaCasos, name='lista_casos'),
    path('nuevo/', views.nuevoCaso, name='nuevo_caso'),
    path('guardar/', views.guardarCaso, name='guardar_caso'),
    path('<int:id>/eliminar/', views.eliminarCaso, name='eliminar_caso'),
    path('<int:id>/editar/', views.editarCaso, name='editar_caso'),
    path('editar/', views.procesarEdicionCaso, name='procesar_edicion_caso'),
]
