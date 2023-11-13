from django.contrib import admin
from .models import contenido,cliente
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#from django.db import models

class contenidoResource(resources.ModelResource):
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
    



# Register your models here.
admin.site.register(contenido,contenidoAdmin)
admin.site.register(cliente,clienteAdmin)






