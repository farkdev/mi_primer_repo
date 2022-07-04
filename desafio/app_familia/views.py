from ast import Delete, Return
from distutils.log import info
from tkinter.font import families
from django.shortcuts import render
from app_familia.models import Apellido, Domicilio, Familias, Avatar
from django.http import HttpResponse
import datetime
from app_familia.forms import UserEditForm, nuevo_formulario, UserEditForm
from django.db.models import Q 
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "index.html", {"url":avatares[0].imagen.url})


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
    

def domicilio (request):
    Direccion = Domicilio.objects.all()
    info = {"info" : Direccion}

    return render(request, "domicilio.html", info)

def adress (request):
    familiares = Domicilio(calle="Carlos Dodero 1699", viviendo_desde = "2000-02-15")
    familiares.save()
    familiares = Domicilio(calle="Carlos Dodero 1699", viviendo_desde = "2000-02-15")
    familiares.save()
    familiares = Domicilio(calle="Liniers 140", viviendo_desde = "1995-11-30")
    familiares.save()

    return HttpResponse("datos guardados")
    

def contacto(request):
    return render(request, "contacto.html")


def data(request):
    info = Apellido.objects.all()
    datas = {"datas" : info}

    return render(request, "arbol.html", datas)

def apellido(request):
    apellidos = Apellido(Apellido_or="Rojas", Pais = "España")
    apellidos.save()
    apellidos = Apellido(Apellido_or = "Konrath", Pais = "Alemania")
    apellidos.save()
  
    return HttpResponse("datos guardados")

@login_required
def nuevo_familiar(request):
    if request.method == "POST":

        miformulario = nuevo_formulario ( request.POST )
        if miformulario.is_valid():
            datos = miformulario.cleaned_data
        
            nuevo = Familias(nombre=datos['nombre'], edad=datos['edad'], nacimiento=datos['nacimiento'], vinculo=datos['vinculo'])
            nuevo.save()
            nuevo = Apellido(Apellido_or=datos['apellido']) 
            nuevo.save()
            nuevo = Domicilio(calle=datos['calle'])
            nuevo.save()
        
        return render(request, "nuevo_familiar.html")
        
    return render(request, "nuevo_familiar.html")


def buscar_familiar (request):

    return render(request, "buscar_familiar.html")

def buscar (request):
    
    if request.GET['buscar']:
        buscar = request.GET['buscar']
        busqueda = Familias.objects.filter(Q(nombre__icontains = buscar)|
        Q(edad__icontains = buscar)|
        Q(nacimiento__icontains = buscar)|
        Q(vinculo__icontains = buscar)
        ).distinct()
    

        
        return render(request, "resultado_busqueda.html", {'busqueda': busqueda})
        
    else:

        return HttpResponse("campo vacío")

@login_required
def eliminar_familiar (request, id):
    eliminar = Familias.objects.get(id=id)
    eliminar.delete()

    eliminar = Familias.objects.all()

    return render(request, "lista_familiares.html", {'eliminar': eliminar})

def modificar(request, id):
    modificar = Familias.objects.get(id=id)
    
    if request.method == "POST":
        miformulario = nuevo_formulario(request.POST)
        
        print(miformulario)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            Familias.nombre = informacion['nombre']
            Familias.edad = informacion['edad']
            Familias.nacimiento = informacion['nacimiento']
            Familias.vinculo = informacion['vinculo']

            Familias.save()

            return render(request, "modificar.html", {'modificar': modificar})

    else:
        miformulario=nuevo_formulario(initial={'nombre':Familias.nombre, 'edad':Familias.edad, 'nacimiento':Familias.nacimiento, 'vinculo':Familias.vinculo})
    render (request, "modificar.html", {"miformulario" : miformulario})


def login_request(request):
    if request.method =="POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido{usuario}"})
                
            else:
                return HttpResponse(f"Usuario incorrecto")

        else: 
            return HttpResponse(f"Incorrecto {form}")    
    



    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})



def register(request):

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
 


    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})

@login_required
def editar_perfil (request):
   
    usuario = request.user

    if request.method =="POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            información = miFormulario.cleaned_data

            usuario.email = información['email']
            password = información['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")



    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render (request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

         

def about_me(request):

    return render(request, "about_me.html")


def template(request):
    return render (request, "template.html")

    
def rojas(request):
    return render (request, "rojas.html")
     
def konrath(request):
    return render (request, "konrath.html")


def perfil(request):
    return render (request, "perfil.html")

def perfil1(request):
    return render (request, "perfil1.html")

def perfil2(request):
 return render (request, "perfil2.html")
 
def perfil3(request):
 return render (request, "perfil3.html")
 
def perfil4(request):
 return render (request, "perfil4.html")

def perfil5(request):
 return render (request, "perfil5.html")

def perfil6(request):
 return render (request, "perfil6.html")
 
def perfil7(request):
 return render (request, "perfil7.html")

def perfil8(request):
 return render (request, "perfil8.html")