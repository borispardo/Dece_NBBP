from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaUsuarios, name='lista_usuarios'),
    path('nuevo/', views.nuevoUsuario, name='nuevo_usuario'),
    path('guardar/', views.guardarUsuario, name='guardar_usuario'),
    path('<int:id>/eliminar/', views.eliminarUsuario, name='eliminar_usuario'),
    path('<int:id>/editar/', views.editarUsuario, name='editar_usuario'),
    path('editar/', views.procesarEdicionUsuario, name='procesar_edicion_usuario'),
]