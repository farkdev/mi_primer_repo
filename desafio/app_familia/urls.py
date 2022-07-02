from django.urls import path, URLPattern
from . import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="index"),
    path("lista_familiares", views.lista_familiares, name= "lista_familiares"),
    path("alta_familiares", views.alta_familiares),
    path("domicilio", views.domicilio, name="domicilio"),
    path("contacto", views.contacto),
    path("arbol", views.data, name = "arbol"),
    path("apellido", views.apellido),
    path("nuevo_familiar", views.nuevo_familiar, name = "nuevo_familiar"),
    path("buscar_familiar", views.buscar_familiar),
    path("buscar", views.buscar),
    path("eliminar_familiar/<int:id>", views.eliminar_familiar, name ="eliminar_familiar"),
    path("login", views.login_request, name="login" ),
    path("registro", views.register, name="registro"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil")

]