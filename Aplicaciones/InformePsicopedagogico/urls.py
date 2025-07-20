from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaInformes, name='lista_informes'),
    path('nuevo/', views.nuevoInforme, name='nuevo_informe'),
    path('guardar/', views.guardarInforme, name='guardar_informe'),
    path('<int:id>/eliminar/', views.eliminarInforme, name='eliminar_informe'),
    path('<int:id>/editar/', views.editarInforme, name='editar_informe'),
    path('editar/', views.procesarEdicionInforme, name='procesar_edicion_informe'),
]