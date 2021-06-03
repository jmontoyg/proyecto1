from django.db import models
from django.db.models import aggregates
from time import time

# Create your models here. ORM

class Usuarios(models.Model):

    ROL = (
        ('1','Administrador'),
        ('2','Barbero'),
        ('3','Cliente')

    )
    idUsuario = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=50, null=False, blank=False)
    correo = models.EmailField(max_length=50, null=False, unique=True)
    contrasena = models.CharField(max_length=50, null=False, blank=False)
    celular = models.CharField(max_length=20, null=False, blank=False)
    rol = models.CharField(max_length=1, choices=ROL, default='3')

    def __str__(self) -> str:
        return self.nombre

class Barberos(models.Model):
    
    idBarbero = models.AutoField(primary_key=True) 
    detalle = models.CharField(max_length=50, null=False, blank=False)
    idUsuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.idUsuario)

def get_upload_file_name(instance, filename):
    return "fotos/%s_%s" %(str(time()).replace('.','_'), filename)
   
class Catalogo(models.Model):
   
    idCatalogo = models.AutoField(primary_key=True) 
    TIPO_CHOISES = (
        ('0','Servicio'),
        ('1','Producto'),
    )
    tipo = models.CharField(max_length=1, null=False, blank=False, choices=TIPO_CHOISES, default='0')
    detalle = models.CharField(max_length=100, null=False, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    foto = models.ImageField('Foto', upload_to=get_upload_file_name)

    def __str__(self) -> str:
        return self.detalle

    
class Reservas(models.Model):
    
    idReserva = models.AutoField(primary_key=True)
    fechaHoraReserva = models.DateTimeField(null=False, blank=False)
    idUsuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    idBarbero = models.ForeignKey(Barberos, on_delete=models.DO_NOTHING)
    idCatalogo = models.ForeignKey(Catalogo, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.idUsuario)




