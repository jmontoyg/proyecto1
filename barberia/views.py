from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Usuarios, Barberos, Catalogo, Reservas
from django.db import IntegrityError
from django.contrib import messages
from django.core.cache import cache



def login(request):

    try:

        q = Usuarios.objects.get(
        correo=request.POST['nombreUsuario'], contrasena=request.POST['contrasena'])
                    # return HttpResponse("Ok", q.rol)
        request.session["login"] = [q.nombre, q.rol, q.correo, q.contrasena, q.idUsuario]
        messages.success(request, 'Sesión iniciada correctamente..!')        

    except Usuarios.DoesNotExist:

        messages.error(request, 'El usuario ingresado no existe!')

    except:

        messages.error(request, 'Usuario o contraseña incorrectos!')
        
    return HttpResponseRedirect(reverse('barberia:index', args=()))

def logout(request):

    try:
        del request.session["login"]
        cache.clear()
        messages.success(request, 'Sesión cerrada correctamente..!')  
        
    except:
        messages.error(request, 'No se pudo cerrar la sesión, por favor intente de nuevo')

    return HttpResponseRedirect(reverse('barberia:index', args=()))

def index(request):
    q = Catalogo.objects.all()
    contexto = {"dato": q}
    return render(request, "barberia/index.html",contexto)


def usuarios(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Usuarios.objects.all()
        contexto = {"datosUsuarios": q}
        return render(request, "barberia/usuarios.html", contexto)
    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def barberos(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Barberos.objects.all()
        contexto = {"datosBarberos": q}
        return render(request, "barberia/barberos.html", contexto)
    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def catalogo(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Catalogo.objects.all()
        contexto = {"datosCatalogo": q}
        return render(request, "barberia/catalogo.html", contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def reservas(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Reservas.objects.all()
        contexto = {"datosReservas": q}
        return render(request, "barberia/reservas.html", contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def productos(request):

    q = Catalogo.objects.all()
    contexto = {"dato": q}
    return render(request, "barberia/productos.html", contexto)


def contacto(request):

    return render(request, "barberia/contacto.html")


def servicios(request):
    q = Catalogo.objects.all()
    contexto = {"dato": q}
    return render(request, "barberia/servicios.html", contexto)


def nosotros(request):

    return render(request, "barberia/nosotros.html")

def reservar(request):

    return render(request, "barberia/reservar.html")


def usuariosFormulario(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        return render(request, "barberia/crear_usuario.html")

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def usuariosGuardar(request):
    if request.method == "POST":

        q = Usuarios(
            nombre=request.POST['nombre'],
            correo=request.POST['correo'],
            contrasena=request.POST['contrasena'],
            celular=request.POST['celular'],
            rol=request.POST['rol']
        )
        q.save()

        messages.success(request, 'Usuario creado correctamente..!')
        

    else:
        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:usuarios', args=()))

def usuariosEliminar(request, id):

    try:

        q = Usuarios.objects.get(pk=id)
        q.delete()
        messages.success(request, 'Usuario eliminado correctamente..!')

    except Usuarios.DoesNotExist:

        messages.error(request, 'El usaurio que intentas eliminar no existe')

    except IntegrityError:

        messages.warning(request, 'No se puede eliminar este usuario porque esta registrado como un Barbero')

    except:

        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:usuarios', args=()))


def usuariosFormularioEditar(request, id):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Usuarios.objects.get(pk=id)
        contexto = {"dato": q}
        return render(request, 'barberia/editar_usuario.html', contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def usuariosEditar(request):

    try: 
        q = Usuarios.objects.get(pk=request.POST['idUsuario'])

        q.nombre = request.POST['nombre']
        q.correo = request.POST['correo']
        q.contrasena = request.POST['contrasena']
        q.celular = request.POST['celular']
        q.rol = request.POST['rol']

        q.save()
        messages.success(request, 'Usuario actualizado correctamente..!')

    except:

        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:usuarios', args=()))


def barberosFormulario(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Usuarios.objects.all()
        contexto = {"dato": q}
        return render(request, "barberia/crear_barbero.html", contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))

def barberosGuardar(request):

    if request.method == "POST":

        r = Usuarios.objects.get(pk=request.POST['nombre'])
        q = Barberos(
            idUsuario=r,
            detalle=request.POST['detalle']
        )

        r.rol = '2'

        q.save()
        r.save()

        messages.success(request, 'Barbero creado correctamente..!')

    else:

        messages.error(request, 'Ha ocurrido un error')
    
    return HttpResponseRedirect(reverse('barberia:barberos', args=()))

def barberosEliminar(request, id, idUsuario):

    try:

        r = Usuarios.objects.get(pk=idUsuario)
        q = Barberos.objects.get(pk=id)
        q.delete()
        r.rol = '3'
        r.save()
        messages.success(request, 'Barbero eliminado correctamente..!')
        
    except Barberos.DoesNotExist:

        messages.error(request, 'El barbero que intentas eliminar no existe')

    except IntegrityError:

        messages.warning(request, 'No se puede eliminar este berbero porque tiene citas reservadas')

    except:

        messages.error(request, 'Ha ocurrido un error')
    
    return HttpResponseRedirect(reverse('barberia:barberos', args=()))


def barberosFormularioEditar(request, id):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Barberos.objects.get(pk=id)

        contexto = {"dato": q}

        return render(request, 'barberia/editar_barbero.html', contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def barberosEditar(request):

    try:

        q = Barberos.objects.get(pk=request.POST['idBarbero'])
        r = Usuarios.objects.get(pk=request.POST['idUsuario'])

        r.nombre = request.POST['nombre']
        q.detalle = request.POST['detalle']

        r.save()
        q.save()

        messages.success(request, 'Barbero actualizado correctamente..!')

    except:

        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:barberos', args=()))


def catalogoFormulario(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        return render(request, "barberia/crear_catalogo.html")

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))

def file_upload(f):
    from django.conf import settings
    from django.core.files.storage import default_storage
    print("Archivo", f)
    print("Ruta: ",settings.MEDIA_ROOT)
    #save_path = os.path.join(settings.MEDIA_ROOT, 'gep/', f)
    save_path = '{0}/{1}'.format(settings.MEDIA_ROOT, f)
    print(save_path)
    
    path = default_storage.save(save_path, f)
    if path:
        print("ok")
    else:
        print("error")
    return f

def catalogoGuardar(request):

    if request.method == "POST":
        
        f = file_upload(request.FILES['foto'])
        q = Catalogo(
            tipo=request.POST['tipo'],
            detalle=request.POST['detalle'],
            valor=request.POST['valor'],
            foto= f
        )
        q.save()
        
        messages.success(request, 'Se ha añadido al catalogo correctamente..!')

    else:

        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:catalogo', args=()))

def catalogoEliminar(request, id):

    try:

        q = Catalogo.objects.get(pk=id)
        q.delete()
        messages.success(request, 'Se ha eliminado correctamente del catalogo..!')

    except Catalogo.DoesNotExist:

        messages.error(request, 'El servicio o producto que intentas eliminar no existe')

    except IntegrityError:

        messages.warning(request, 'No se puede eliminar este servicio porque esta asigando a una cita reservada')

    except:

        messages.error(request, 'Ha ocurrido un error')
    
    return HttpResponseRedirect(reverse('barberia:catalogo', args=()))


def catalogoFormularioEditar(request, id):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Catalogo.objects.get(pk=id)
        contexto = {"dato": q}
        return render(request, 'barberia/editar_catalogo.html', contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def catalogoEditar(request):

    try:

        q = Catalogo.objects.get(pk=request.POST['idCatalogo'])
        f = file_upload(request.FILES['foto'])

        q.tipo = request.POST['tipo']
        q.detalle = request.POST['detalle']
        q.valor = request.POST['valor']
        q.foto = f

        q.save()
        messages.success(request, 'Se ha actualizado correctamente en el catalogo..!')

    except:

        messages.error(request, 'Ha ocurrido un error')
    
    return HttpResponseRedirect(reverse('barberia:catalogo', args=()))


def reservaFormulario(request):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Barberos.objects.all()
        r = Usuarios.objects.all()
        s = Catalogo.objects.all()

        contexto = {"dato": q, "datosUsuarios": r, "datosCatalogo": s}
        return render(request, "barberia/crear_reserva.html", contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def reservaGuardar(request):

    if request.method == "POST":

        q = Reservas(
            fechaHoraReserva=request.POST['fecha'],
            idUsuario=Usuarios.objects.get(pk=request.POST['cliente']),
            idBarbero=Barberos.objects.get(pk=request.POST['barbero']),
            idCatalogo=Catalogo.objects.get(pk=request.POST['servicio'])
        )
        q.save()
        
        messages.success(request, 'La cita se ha reservado correctamente..!')

    else:

        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:reservas', args=()))

def reservaEliminar(request, id):

    try:

        q = Reservas.objects.get(pk=id)
        q.delete()
        messages.success(request, 'Se ha eliminado correctamente la reserva..!')

    except Reservas.DoesNotExist:

        messages.error(request, 'La reserva que intentas eliminar no existe')     

    except:

        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:reservas', args=()))

def reservaFormularioEditar(request, id):

    logueado = request.session.get('login', False)

    if logueado and (logueado[1] == '1' or logueado[1] == '2'):

        q = Reservas.objects.get(pk=id)
        t = Barberos.objects.all()
        r = Usuarios.objects.all()
        s = Catalogo.objects.all()

        contexto = {"dato": q, "datosUsuarios": r, "datosCatalogo": s, "datosBarberos": t}

        return render(request, 'barberia/editar_reserva.html', contexto)

    else:
        return HttpResponseRedirect(reverse('barberia:index', args=()))


def reservaEditar(request):

    try:

        q = Reservas.objects.get(pk=request.POST['idReserva'])

        q.fechaHoraReserva = request.POST['fecha']
        q.idUsuario = Usuarios.objects.get(pk=request.POST['cliente'])
        q.idBarbero = Barberos.objects.get(pk=request.POST['barbero'])
        q.idCatalogo = Catalogo.objects.get(pk=request.POST['servicio'])

        q.save()
        messages.success(request, 'Se ha actualizado correctamente la reserva..!')

    except:

        messages.error(request, 'Ha ocurrido un error')

    return HttpResponseRedirect(reverse('barberia:reservas', args=()))


def holaMundo(request):
    return HttpResponse("Hola Mundo <br> <a href='../saludar'>Prueba</a>")


def saludar(request):
    return HttpResponse("<h1>Hola desde mi aplicación BARBERÍA</h1>")


def editarUsuario(request, id):
    return HttpResponse("Ok, digitaste: %s" % id)
