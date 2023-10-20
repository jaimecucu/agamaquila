from django.db import models

# Create your models here.

from datetime import datetime

# Create your models here.
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

