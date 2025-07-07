from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaDocentes, name='lista'),
    path('nuevo/', views.nuevoDocente, name='nuevo'),
    path('guardar/', views.guardarDocente, name='guardar'),
    path('<int:id>/eliminar/', views.eliminarDocente, name='eliminar'),
    path('<int:id>/editar/', views.editarDocente, name='editar'),
    path('editar/', views.procesarEdicionDocente, name='procesarEdicion'),
]