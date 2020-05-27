from django.contrib import admin

# Register your models here.

from SGBD.models import Empleado, Animal, Alimentacion
admin.site.register(Empleado)
admin.site.register(Animal)
admin.site.register(Alimentacion)
