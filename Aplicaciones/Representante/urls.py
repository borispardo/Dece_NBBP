from django.urls import path
from . import views
urlpatterns = [
    path('', views.listaRepresentantes, name='lista'),
    path('nuevo/', views.nuevoRepresentante, name='nuevo'),
    path('guardar/', views.guardarRepresentante, name='guardar'),
    path('<int:id>/eliminar/', views.eliminarRepresentante, name='eliminar'),
    path('<int:id>/editar/', views.editarRepresentante, name='editar'),
    path('editar/', views.procesarEdicionRepresentante, name='procesarEdicion'),
]