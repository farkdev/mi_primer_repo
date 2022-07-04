from django.contrib import admin

from app_familia.views import domicilio
from .models import *
# Register your models here.


admin.site.register(Familias)
admin.site.register(Domicilio)
admin.site.register(Apellido)
admin.site.register(Avatar)
