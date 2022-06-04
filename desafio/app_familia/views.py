from django.shortcuts import render
from app_familia.models import Familias
from django.http import HttpResponse
import datetime



# Create your views here.

def inicio(request):
    return render(request, "index.html")


def lista_familiares(request):
    miembros = Familias.objects.all()
    datos = {"datos": miembros}
    return render(request, "lista_familiares.html", datos)
 

def alta_familiares(request):
    familiar = Familias(nombre="José", edad=51, nacimiento="1970-11-23", vinculo = "papa")
    familiar.save()
    familiar = Familias(nombre="Miriam", edad=50, nacimiento="1971-10-26", vinculo = "mama")
    familiar.save()
    familiar = Familias(nombre="Mica", edad=26, nacimiento="1995-11-30", vinculo = "novia")
    familiar.save()

    return HttpResponse("Se creo correctamente")
    