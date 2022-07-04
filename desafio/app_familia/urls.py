from django.urls import path, URLPattern
from . import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="index"),
    path("lista_familiares", views.lista_familiares, name= "lista_familiares"),
    path("alta_familiares", views.alta_familiares),
    path("domicilio", views.domicilio, name="domicilio"),
    path("contacto", views.contacto, name = "contacto"),
    path("arbol", views.data, name = "arbol"),
    path("apellido", views.apellido),
    path("nuevo_familiar", views.nuevo_familiar, name = "nuevo_familiar"),
    path("buscar_familiar", views.buscar_familiar, name ="buscar_familiar"),
    path("buscar", views.buscar),
    path("eliminar_familiar/<int:id>", views.eliminar_familiar, name ="eliminar_familiar"),
    path("login", views.login_request, name="login" ),
    path("registro", views.register, name="registro"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
    path("about_me", views.about_me, name="about_me"),
    path("modificar/<int:id>", views.modificar, name ="modificar"),
    path("template", views.template, name = "template"),
    path("rojas", views.rojas, name = "rojas"),
    path("konrath", views.konrath, name ="konrath"),
    path("perfil", views.perfil, name = "perfil"),
    path("perfil1", views.perfil1, name = "perfil1"),
    path("perfil2", views.perfil2, name = "perfil2"),
    path("perfil3", views.perfil3, name = "perfil3"),
    path("perfil4", views.perfil4, name = "perfil4"),
    path("perfil5", views.perfil5, name = "perfil5"),
    path("perfil6", views.perfil6, name = "perfil6"),
    path("perfil7", views.perfil7, name = "perfil7"),
    path("perfil8", views.perfil8, name = "perfil8")

]