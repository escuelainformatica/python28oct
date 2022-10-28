from django.db.models import Model
from django.shortcuts import render

from app1.models import Person


# Create your views here.
def listar_person(request):
    personas=Person.objects.all()  # estoy trayendo todas las filas de la tabla persona

    return render(request,'listar_person.html',{"personas":personas})