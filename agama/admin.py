from django.contrib import admin
from .models import contenido,cliente,Tarima,contenido2,Tarima2
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#from django.db import models

class clienteResource(resources.ModelResource):
    class Meta:
        model = cliente


class clienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombre_cliente']    
    list_display= ['nombre_cliente']
    #resources_class=clienteResource



class contenidoResource(resources.ModelResource):
    class Meta:
        model = contenido


class contenidoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombre_cliente']
    list_display= ['nombre_cliente','fecha_registro','hora_registro',]


    resources_class=contenidoResource



class TarimaResource(resources.ModelResource):
    class Meta:
        model = Tarima


class TarimaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['producto_tarima']    
    list_display= ['producto_tarima']

class contenido2Resource(resources.ModelResource):
    class Meta:
        model = contenido2


class contenido2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombre_cliente']
    list_display= ['nombre_cliente','fecha_registro','hora_registro',]


    resources_class=contenido2Resource

class Tarima2Resource(resources.ModelResource):
    class Meta:
        model = Tarima2


class Tarima2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['producto_tarima']    
    list_display= ['producto_tarima']
    





    



# Register your models here.
admin.site.register(contenido,contenidoAdmin)
admin.site.register(cliente,clienteAdmin)
admin.site.register(Tarima,TarimaAdmin)
admin.site.register(contenido2,contenido2Admin)
admin.site.register(Tarima2,Tarima2Admin)







