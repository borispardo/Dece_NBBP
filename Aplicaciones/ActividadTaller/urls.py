from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaTalleres, name='lista_talleres'),
    path('nuevo/', views.nuevoTaller, name='nuevo_taller'),
    path('guardar/', views.guardarTaller, name='guardar_taller'),
    path('<int:id>/editar/', views.editarTaller, name='editar_taller'),
    path('<int:id>/actualizar/', views.procesarEdicionTaller, name='procesar_taller'),
    path('eliminar/<int:id>/', views.eliminarTaller, name='eliminar_taller'),
]
