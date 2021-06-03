from django.urls import path

from . import views

app_name = 'barberia'

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('barberos/', views.barberos, name='barberos'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('reservas/', views.reservas, name='reservas'),
    path('servicios/', views.servicios, name='servicios'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('reservar/', views.reservar, name='reservar'),
    path('crear_usuario/', views.usuariosFormulario, name='crear_usuario'),
    path('guardar_usuario/', views.usuariosGuardar, name='guardar_usuario'),
    path('eliminar_usuario/<int:id>/', views.usuariosEliminar, name='eliminar_usuario'),
    path('formulario_editar_usuario/<int:id>/', views.usuariosFormularioEditar, name='formulario_editar_usuario'),
    path('editar_usuario/', views.usuariosEditar, name='editar_usuario'),
    path('crear_barbero/', views.barberosFormulario, name='crear_barbero'),
    path('guardar_barbero/', views.barberosGuardar, name='guardar_barbero'),
    path('eliminar_barbero/<int:id>/<int:idUsuario>', views.barberosEliminar, name='eliminar_barbero'),
    path('formulario_editar_barbero/<int:id>/', views.barberosFormularioEditar, name='formulario_editar_barbero'),
    path('editar_barbero/', views.barberosEditar, name='editar_barbero'),
    path('crear_catalogo/', views.catalogoFormulario, name='crear_catalogo'),
    path('guardar_catalogo/', views.catalogoGuardar, name='guardar_catalogo'),
    path('eliminar_catalogo/<int:id>/', views.catalogoEliminar, name='eliminar_catalogo'),
    path('formulario_editar_catalogo/<int:id>/', views.catalogoFormularioEditar, name='formulario_editar_catalogo'),
    path('editar_catalogo/', views.catalogoEditar, name='editar_catalogo'),
    path('crear_reserva/', views.reservaFormulario, name='crear_reserva'),
    path('guardar_reserva/', views.reservaGuardar, name='guardar_reserva'),
    path('eliminar_reserva/<int:id>/', views.reservaEliminar, name='eliminar_reserva'),
    path('formulario_editar_reserva/<int:id>/', views.reservaFormularioEditar, name='formulario_editar_reserva'),
    path('editar_reserva/', views.reservaEditar, name='editar_reserva'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('hola/', views.holaMundo, name='hola'),
    path('saludar/', views.saludar, name='saludar'),
    path('editar/<int:id>', views.editarUsuario, name='editar'),
]