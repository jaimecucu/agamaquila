from django.db import models
from django.db.models import deletion
from django.core.exceptions import ValidationError

# Create your models here.

from datetime import datetime

# Create your models here.

class cliente(models.Model):    
    nombre_cliente = models.CharField('Nombre del cliente',max_length=100, unique=True)
    direccion_fiscal = models.CharField('Direccion fiscal',max_length=100, default='')
    contacto_dir = models.CharField('Contacto',max_length=100, default='')
    

    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'

    def __srt__(self):
        return self.nombre_cliente 
    

class contenido(models.Model):   
    #datos del cliente
    fecha_registro = models.DateField(auto_now_add=True)
    hora_registro =  models.TimeField(auto_now_add=True) 
    nombre_cliente = models.CharField('Nombre del cliente',max_length=100, default='')
    direccion_fiscal = models.CharField('Direccion fiscal',max_length=100, default='')
    contacto_dir = models.CharField('Contacto',max_length=100, default='')

    #datos del transporte parte 1
    empresa_transportadora = models.CharField('Empresa transportadora',max_length=100, default='')
    nombre_transportista = models.CharField('Nombre del transportista',max_length=100, default='')
    licencia = models.CharField('No. de licencia',max_length=100, default='')
    certificado_fumigacion = models.CharField('Certificado de fumigacion',max_length=100, default='')  

    #datos del transporte parte 2
    tracto_camion = models.CharField('Tracto camion',max_length=100, default='')
    placas_unidad = models.CharField('Placas de la unidad',max_length=100, default='')
    placas_caja = models.CharField('Placas de la caja',max_length=100, default='')
    numero_caja = models.CharField('No. Caja',max_length=100, default='')

    #producto entregado
    producto = models.CharField('Producto',max_length=100, default='') 
    cantidad_charolas = models.CharField('Cantidad total de charolas',max_length=100, default='')
    numero_lote = models.CharField('Numero de lote',max_length=100, default='')
    cantidad_tarimas = models.CharField('Cantidad total de tarimas',max_length=100, default='')

    #puntos de revision 
    #pisos en buen estado
    sin_hoyos = models.CharField('Charolas',max_length=10, default='')
    sin_parches = models.CharField('Charolas',max_length=10, default='')
    sin_salientes = models.CharField('Charolas',max_length=10, default='')
    sin_laminas = models.CharField('Charolas',max_length=10, default='')

    #puertas en buen estado
    puertas_empaques = models.CharField('Charolas',max_length=10, default='')
    puertas_hermetico = models.CharField('Charolas',max_length=10, default='')
    puertas_salientes= models.CharField('Charolas',max_length=10, default='')
    puertas_laminas = models.CharField('Charolas',max_length=10, default='')

    #condiciones de higiene

    higiene_limpios = models.CharField('Charolas',max_length=10, default='')
    higiene_olores = models.CharField('Charolas',max_length=10, default='')
    higiene_plagas = models.CharField('Charolas',max_length=10, default='')

    #paredes en buen estado

    paredes_hoyos = models.CharField('Charolas',max_length=10, default='')
    paredes_parches = models.CharField('Charolas',max_length=10, default='')
    paredes_salientes= models.CharField('Charolas',max_length=10, default='')
    paredes_laminas = models.CharField('Charolas',max_length=10, default='')

    #techos en buen estado
    techos_hoyos = models.CharField('Charolas',max_length=10, default='')
    techos_salientes = models.CharField('Charolas',max_length=10, default='')
    techos_laminas = models.CharField('Charolas',max_length=10, default='')

    #condiciones externas
    externas_llantas = models.CharField('Charolas',max_length=10, default='')
    externas_refaccion = models.CharField('Charolas',max_length=10, default='')
    externas_patines = models.CharField('Charolas',max_length=10, default='')
    externas_luces = models.CharField('Charolas',max_length=10, default='')
    externas_tanque = models.CharField('Charolas',max_length=10, default='')

    #CONDICIONES VISUALES DE LA UNIADA
    visual_paredes = models.ImageField('Paredes',upload_to='imagenes/', default='')
    visual_piso = models.ImageField('Piso',upload_to='imagenes/', default='')
    visual_techo = models.ImageField('Techo',upload_to='imagenes/', default='') 
    hora_llegada = models.CharField('Hora de llegada',max_length=100, default='')
    hora_salida = models.CharField('Hora de salida',max_length=100, default='') 

    #CONDICIONES VISUALES DEL PRODUCTO DE ENTREGA  
    visual_tarima1 = models.ImageField('Primer tarima',upload_to='imagenes/', default='')
    visual_mitad_carga = models.ImageField('Mitad de carga',upload_to='imagenes/', default='')
    visual_fin_carga = models.ImageField('Fin de carga',upload_to='imagenes/', default='')
    visual_cerrado_unidad = models.ImageField('Cerrado de la unidad',upload_to='imagenes/', default='')
    hora_inicio_carga = models.CharField('Hora inicio de carga',max_length=100, default='')
    hora_fin_carga = models.CharField('Hora fin de carga',max_length=100, default='')

    

    class Meta:
        verbose_name='contenido'
        verbose_name_plural='contenidos'

    def __srt__(self):
        return self.nombre_cliente 
    


class Tarima(models.Model):

    
    numero_tarima = models.IntegerField('Numero de Tarima', unique=False)    
    lote_tarima = models.CharField('Numero de lote',max_length=50, default='')    
    producto_tarima = models.CharField('Producto',max_length=150, default='')
    camas_tarima = models.IntegerField('Numero de camas', unique=False)
    paquetes_tarima = models.IntegerField('Numero de paquetes', unique=False)
    latas_tarima = models.CharField('Lata',max_length=5, default='')
    charolas_tarima = models.CharField('Charolas',max_length=5, default='')
    emplayado_tarima = models.CharField('Emplayado',max_length=5, default='')
    observaciones_tarima = models.CharField('Observaciones',max_length=200, default='')
    

    class Meta:
        verbose_name='Tarima'
        verbose_name_plural='Tarimas'

    def __srt__(self):
        return self.producto_tarima 
    

class contenido2(models.Model):   
    #datos del cliente
    fecha_registro = models.DateField(auto_now_add=True)
    hora_registro =  models.TimeField(auto_now_add=True) 
    nombre_cliente = models.CharField('Nombre del cliente',max_length=100, default='')
    direccion_fiscal = models.CharField('Direccion fiscal',max_length=100, default='')
    contacto_dir = models.CharField('Contacto',max_length=100, default='')

    #datos del transporte parte 1
    empresa_transportadora = models.CharField('Empresa transportadora',max_length=100, default='')
    nombre_transportista = models.CharField('Nombre del transportista',max_length=100, default='')
    licencia = models.CharField('No. de licencia',max_length=100, default='')
    certificado_fumigacion = models.CharField('Certificado de fumigacion',max_length=100, default='')  

    #datos del transporte parte 2
    tracto_camion = models.CharField('Tracto camion',max_length=100, default='')
    placas_unidad = models.CharField('Placas de la unidad',max_length=100, default='')
    placas_caja = models.CharField('Placas de la caja',max_length=100, default='')
    numero_caja = models.CharField('No. Caja',max_length=100, default='')

    #producto entregado
    producto = models.CharField('Producto',max_length=100, default='') 
    cantidad_charolas = models.CharField('Cantidad total de charolas',max_length=100, default='')
    numero_lote = models.CharField('Numero de lote',max_length=100, default='')
    cantidad_tarimas = models.CharField('Cantidad total de tarimas',max_length=100, default='')

    #puntos de revision 
    #pisos en buen estado
    sin_hoyos = models.CharField('Charolas',max_length=10, default='')
    sin_parches = models.CharField('Charolas',max_length=10, default='')
    sin_salientes = models.CharField('Charolas',max_length=10, default='')
    sin_laminas = models.CharField('Charolas',max_length=10, default='')

    #puertas en buen estado
    puertas_empaques = models.CharField('Charolas',max_length=10, default='')
    puertas_hermetico = models.CharField('Charolas',max_length=10, default='')
    puertas_salientes= models.CharField('Charolas',max_length=10, default='')
    puertas_laminas = models.CharField('Charolas',max_length=10, default='')

    #condiciones de higiene

    higiene_limpios = models.CharField('Charolas',max_length=10, default='')
    higiene_olores = models.CharField('Charolas',max_length=10, default='')
    higiene_plagas = models.CharField('Charolas',max_length=10, default='')

    #paredes en buen estado

    paredes_hoyos = models.CharField('Charolas',max_length=10, default='')
    paredes_parches = models.CharField('Charolas',max_length=10, default='')
    paredes_salientes= models.CharField('Charolas',max_length=10, default='')
    paredes_laminas = models.CharField('Charolas',max_length=10, default='')

    #techos en buen estado
    techos_hoyos = models.CharField('Charolas',max_length=10, default='')
    techos_salientes = models.CharField('Charolas',max_length=10, default='')
    techos_laminas = models.CharField('Charolas',max_length=10, default='')

    #condiciones externas
    externas_llantas = models.CharField('Charolas',max_length=10, default='')
    externas_refaccion = models.CharField('Charolas',max_length=10, default='')
    externas_patines = models.CharField('Charolas',max_length=10, default='')
    externas_luces = models.CharField('Charolas',max_length=10, default='')
    externas_tanque = models.CharField('Charolas',max_length=10, default='')

    #CONDICIONES VISUALES DE LA UNIADA
    visual_paredes = models.ImageField('Paredes',upload_to='imagenes/', default='')
    visual_piso = models.ImageField('Piso',upload_to='imagenes/', default='')
    visual_techo = models.ImageField('Techo',upload_to='imagenes/', default='') 
    hora_llegada = models.CharField('Hora de llegada',max_length=100, default='')
    hora_salida = models.CharField('Hora de salida',max_length=100, default='') 

    #CONDICIONES VISUALES DEL PRODUCTO DE ENTREGA  
    visual_tarima1 = models.ImageField('Primer tarima',upload_to='imagenes/', default='')
    visual_mitad_carga = models.ImageField('Mitad de carga',upload_to='imagenes/', default='')
    visual_fin_carga = models.ImageField('Fin de carga',upload_to='imagenes/', default='')
    visual_cerrado_unidad = models.ImageField('Cerrado de la unidad',upload_to='imagenes/', default='')
    hora_inicio_carga = models.CharField('Hora inicio de carga',max_length=100, default='')
    hora_fin_carga = models.CharField('Hora fin de carga',max_length=100, default='')

    class Meta:
        verbose_name='contenido2'
        verbose_name_plural='contenidos2'

    def __srt__(self):        
        return self.nombre_cliente 

class Tarima2(models.Model):

    
    numero_tarima = models.IntegerField('Numero de Tarima', unique=False)    
    lote_tarima = models.CharField('Numero de lote',max_length=50, default='')    
    producto_tarima = models.CharField('Producto',max_length=150, default='')
    camas_tarima = models.IntegerField('Numero de camas', unique=False)
    paquetes_tarima = models.IntegerField('Numero de paquetes', unique=False)
    latas_tarima = models.CharField('Lata',max_length=5, default='')
    charolas_tarima = models.CharField('Charolas',max_length=5, default='')
    emplayado_tarima = models.CharField('Emplayado',max_length=5, default='')
    observaciones_tarima = models.CharField('Observaciones',max_length=200, default='')
    contenido2 = models.ForeignKey(contenido2, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name='Tarima2'
        verbose_name_plural='Tarimas2'

    def __srt__(self):
        return self.producto_tarima 
    
 


    


