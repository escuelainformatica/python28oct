from django.db.models import Model
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect

from app1.models import Person, Pais


# Create your views here.
def listar_person(request):
    personas = Person.objects.all()  # estoy trayendo todas las filas de la tabla persona
    print(personas)
    return render(request, 'listar_person.html', {"personas": personas})


def home(request: HttpRequest):
    return render(request, 'home.html')


def formulario_person(request: HttpRequest):
    # 1) leer los valores que digito el usuario, si no hay datos, se asignan valores por defecto
    persona = Person()
    persona.first_name = request.POST.get('first_name', '')
    persona.last_name = request.POST.get('last_name', '')
    persona.edad = request.POST.get('edad', 0)

    boton = request.POST.get('boton', '')
    if (boton != ''):  # insertar en la base de datos una persona nueva
        persona.save()  # insertar en la base de datos
        return redirect('/person/listar')  # redireccionar.

    # en caso de que no se presiono el boton, muestro los datos
    return render(request, 'formulario_person.html', {'persona': persona})

def listar_pais(request: HttpRequest):
    paises=Pais.objects.all()
    return render(request,'listar_pais.html',{'paises':paises})

def pais_actualizar(request: HttpRequest,idpais:int):
    # 1) leer los datos desde la base de datos.
    pais=Pais.objects.get(id=idpais) # leo el pais con el id igual a idpais

    boton = request.POST.get('boton', '')
    if boton!="": # se presiono el boton?
        pais.nombre=request.POST.get('nombre')
        pais.save() # esto va a actualizar, ya que pais.id no es None.
        return redirect('/pais/listar')

    return render(request,'pais_actualizar.html',{"pais":pais})

def pais_borrar(request: HttpRequest, idpais:int):
    pais = Pais.objects.get(id=idpais)  # leo el pais con el id igual a idpais
    pais.delete()
    return redirect('/pais/listar')
def pais_insertar(request: HttpRequest):
    # 1) leo los datos del usuario en un objeto llamado pais.
    pais=Pais()
    pais.id = request.POST.get('id', None)
    pais.nombre=request.POST.get('nombre','')
    # 2) si se presiono el boton, insertar los datos, y redireccionar al listado.
    boton=request.POST.get('boton','')
    if boton!='':
        pais.save() # guardar en la base de datos. Si id=None entonces inserta, o sino actualiza.
        return redirect('/pais/listar')
    # el boton no se presiono, solo mostrar los datos.
    return render(request,'pais_insertar.html',{'pais':pais})