from django.contrib import admin

from .models import Usuarios, Barberos, Catalogo, Reservas
from django.utils.html import format_html


class UsuariosAdmin(admin.ModelAdmin):
    # fields = ['nombre', 'celular', 'correo', 'contrasena']
    fieldsets = [
        ('Datos personales',               {'fields': ['nombre', 'celular']}),
        ('Datos de usuario', {'fields': ['correo', 'contrasena', 'rol']}),
    ]

    list_display = ('nombre', 'celular', 'correo', 'contrasena', 'rol')
    list_filter = ['nombre']
    search_fields = ['nombre', 'correo']
    # list_editable = ['celular']

class BarberosAdmin(admin.ModelAdmin):

    list_display = ('idUsuario', 'detalle')
    list_filter = ['idUsuario']
    search_fields = ['idUsuario']

class CatalogoAdmin(admin.ModelAdmin):
    
    list_display = ('tipo', 'detalle', 'valor', 'verFoto')
    list_filter = ['detalle']
    search_fields = ['detalle']

    def verFoto(self, obj):
        return format_html('<img src="{}" width="100" />', obj.foto.url )

class ReservasAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Fecha y hora de reserva',               {'fields': ['fechaHoraReserva']}),
        ('Datos de la reserva', {'fields': ['idUsuario', 'idBarbero', 'idCatalogo']}),
    ]
    list_display = ('fechaHoraReserva', 'idUsuario', 'idBarbero', 'idCatalogo')
    list_filter = ['fechaHoraReserva']
    search_fields = ['idUsuario', 'idCatalogo', 'idBarbero']


admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Barberos, BarberosAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Reservas, ReservasAdmin)
