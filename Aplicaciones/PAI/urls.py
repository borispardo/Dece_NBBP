from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaPais, name='lista_pais'),
    path('nuevo/', views.nuevoPAI, name='nuevo_pai'),
    path('guardar/', views.guardarPAI, name='guardar_pai'),
    path('<int:id>/eliminar/', views.eliminarPAI, name='eliminar_pai'),
    path('<int:id>/editar/', views.editarPAI, name='editar_pai'),
    path('editar/', views.procesarEdicionPAI, name='procesar_edicion_pai'),
]
