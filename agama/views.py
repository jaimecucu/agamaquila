from email import utils
from io import BytesIO
from mmap import PAGESIZE
import reportlab
from django.shortcuts import render,redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape,letter
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Table,TableStyle
from  django.templatetags.static import  static
import subprocess
from .forms import contenidoForm,clientesForm,TarimaForm,contenido_terminarForm#,transporteForm,transporte1Form,productoForm,producto1Form,visualForm,visual1Form,visual_productoForm,visual_producto1Form
from .models import contenido,cliente,Tarima,contenido2,Tarima2
from django.conf import settings
import  os
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.views.generic import View
from django.http import JsonResponse
import json
from collections import Counter
from reportlab.lib import colors
from reportlab.lib.units import cm
#direccion local
#imagen_media12="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"
#direccion produccion
imagen_media12="/maquilas/media/"












#from django.template.loader import render_to_string
# Create your views here.

def menuaga(request):  
    return render(request,'base.html')

def finalizarRegistro(request): 
    
    # Obtienes los datos de la primera tabla
    datos = contenido.objects.all()
    # Los conviertes en una lista de objetos de la segunda tabla
    nuevos_datos = [contenido2(**{k: v for k, v in dato.__dict__.items() if k != '_state'}) for dato in datos]
    # Los insertas en la segunda tabla
    contenido2.objects.bulk_create(nuevos_datos)
    # Borras los datos de la primera tabla
    contenido.objects.all().delete()
    # Obtener los datos del modelo tarima
    datos_tarima = Tarima.objects.values()

    # Obtener el id del último registro del modelo contenido2
    id_contenido2 = contenido2.objects.last().id

    # Crear una lista vacía para almacenar las nuevas instancias de tarima2
    nuevas_tarimas = []

    # Iterar sobre los datos de tarima y agregar el id de contenido2
    for dato2 in datos_tarima:

        dato2['contenido2_id'] = id_contenido2
        # Crear una nueva instancia de tarima2 con el dato combinado
        nueva_tarima = Tarima2(**dato2)
        # Agregar la nueva instancia a la lista
        nuevas_tarimas.append(nueva_tarima)

    # Guardar las nuevas instancias de tarima2 en la base de datos
    Tarima2.objects.bulk_create(nuevas_tarimas)
    Tarima.objects.all().delete()
        
    return redirect('embarque')


def limpiarTabla(request):
    # Obtiene una lista de los objetos a borrar
    contenidos = contenido.objects.all().first()

    imagen1 = contenidos.visual_paredes
    imagen2 = contenidos.visual_piso
    imagen3= contenidos.visual_techo
    imagen4= contenidos.visual_tarima1
    imagen5= contenidos.visual_mitad_carga
    imagen6= contenidos.visual_fin_carga
    imagen7= contenidos.visual_cerrado_unidad

    ruta_imagen1 ="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"+ str(imagen1)
    ruta_imagen2 ="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"+ str(imagen2)
    ruta_imagen3 ="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"+ str(imagen3)
    ruta_imagen4 ="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"+ str(imagen4)
    ruta_imagen5 ="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"+ str(imagen5)
    ruta_imagen6 ="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"+ str(imagen6)
    ruta_imagen7 ="C:/Users/uzzie/Desktop/proyecto-D3/maquilas/maquilas/media/"+ str(imagen7)

    
    # Lista de archivos a eliminar
    archivos = [ruta_imagen1, ruta_imagen2, ruta_imagen3, ruta_imagen4, ruta_imagen5, ruta_imagen6, ruta_imagen7]
    # Bucle for para eliminar cada archivo
    import os
    for archivo in archivos:
        os.remove(archivo) 
    Tarima.objects.all().delete()
    contenido.objects.all().delete()
    return redirect('embarque')
    


def registroCliente(request):  
    data = {
        'form':clientesForm()
        
    }

    if request.method == 'POST':
        contenido_form=clientesForm(request.POST)
        nom = request.POST['nombre_cliente']      

        comprocliete=cliente.objects.filter(nombre_cliente =nom)     
    
        if comprocliete:
             
             messages.error(request, "El cliente ya existe.")        

        else: #contenido_form.is_valid()
            
            contenido_form.save() 
            messages.success(request, "Operacion exitosa.")           
        #messages.success(request, "Tu accion fue exitosa.")       
            
    return render(request,'registro-cliente.html',data)



def registroTarima(request):
   

    data = {
        'form':TarimaForm()
        
    }

    if request.method == 'POST':

        tarima_form=TarimaForm(request.POST)
        
        
        

        if tarima_form.is_valid():
            tarima_form.save()
            data['num_tarimas'] = Tarima.objects.count() # obtiene el número de registros de Tarima
            
            return render(request,'registro-tarima.html',data)
            
            
            #data["mensaje"] = "datos guardados"
            
            
        else:

           
            #return render(request,'registro-tarima.html')
            
            #return render(request,'registro-tarima.html',data)
            data["form"]=tarima_form
    data['num_tarimas'] = Tarima.objects.count() # obtiene el número de registros de Tarima
            
                    
    return render(request,'registro-tarima.html',data)





def registro_salida(request):
    data = {
        'form':contenido_terminarForm()
        
    }

    if request.method == 'POST':
        
        unidad = contenido.objects.last()
        contenido_form = contenido_terminarForm(request.POST.copy(), instance=unidad) # Creamos el formulario con los datos del objeto
           

          
    
        if contenido_form.is_valid(): # Validamos el formulario
            contenido_form.save() # Guardamos los cambios en el objeto
             # Obtienes los datos de la primera tabla
            datos = contenido.objects.all()
            # Los conviertes en una lista de objetos de la segunda tabla
            nuevos_datos = [contenido2(**{k: v for k, v in dato.__dict__.items() if k != '_state'}) for dato in datos]
            # Los insertas en la segunda tabla
            contenido2.objects.bulk_create(nuevos_datos)
            # Borras los datos de la primera tabla
            contenido.objects.all().delete()
            # Obtener los datos del modelo tarima
            datos_tarima = Tarima.objects.values()

            # Obtener el id del último registro del modelo contenido2
            id_contenido2 = contenido2.objects.last().id

            # Crear una lista vacía para almacenar las nuevas instancias de tarima2
            nuevas_tarimas = []

            # Iterar sobre los datos de tarima y agregar el id de contenido2
            for dato2 in datos_tarima:

                dato2['contenido2_id'] = id_contenido2
                # Crear una nueva instancia de tarima2 con el dato combinado
                nueva_tarima = Tarima2(**dato2)
                # Agregar la nueva instancia a la lista
                nuevas_tarimas.append(nueva_tarima)

            # Guardar las nuevas instancias de tarima2 en la base de datos
            Tarima2.objects.bulk_create(nuevas_tarimas)
            Tarima.objects.all().delete()
            return redirect('embarque') # Redirigimos a la lista de unidades   
    return render(request,'registro-salida.html',data)








    



    
    
     
    
    

   


    





def embarque(request):
   

    data = {
        'form':contenidoForm()
        
    }

    if request.method == 'POST':

        contenido_form=contenidoForm(request.POST,request.FILES)
        print(contenido_form)

        if contenido_form.is_valid():
            contenido_form.save()
            return redirect('registroTar')
            
            #data["mensaje"] = "datos guardados"
            
            
        else:
            data["form"]=contenido_form
    return render(request,'registro.html',data)

def listarCliente(request):     
    clientes= cliente.objects.all().order_by('-id')[:5]    
    return render(request,'clientes-lista.html',{'clientes': clientes})

def listarTarimas(request):     
    Tarimas= Tarima.objects.all().order_by('-id')[:30]    
    return render(request,'tarimas-lista.html',{'Tarimas': Tarimas})

def listarTarimas2(request):     
    Tarimas= Tarima2.objects.all().order_by('-id')[:30]    
    return render(request,'tarimas2-lista.html',{'Tarimas2': Tarimas})






def consulta_clientes(request):
    termino = request.GET.get('name', '')
    
    # Obtener los cinco últimos clientes ordenados por id
    clientes = cliente.objects.filter(nombre_cliente__icontains=termino).order_by("-id")[:5]
    # Crear una lista vacía
    data = []
    # Recorrer los clientes y agregarlos a la lista como diccionarios
    for Cliente in clientes:
        data.append({
            "id": Cliente.id,
            "nombre_cliente": Cliente.nombre_cliente,
            "direccion_fiscal": Cliente.direccion_fiscal,
            "contacto_dir": Cliente.contacto_dir
        })
    # Devolver los datos en formato JSON
    return JsonResponse(data, safe=False)

def consulta_cliente(request):
  # Obtener el id del cliente del parámetro GET
  id = request.GET.get("id")  
  # Obtener el cliente de la base de datos
  Cliente = cliente.objects.get(id=id)
  # Crear un diccionario con los datos del cliente
  data = {
    "nombre_cliente": Cliente.nombre_cliente,
    "direccion_fiscal": Cliente.direccion_fiscal,
    "contacto_dir": Cliente.contacto_dir
  }
  # Convertir el diccionario a una cadena JSON
  data_json = json.dumps(data)
  # Devolver la cadena JSON como respuesta
  return HttpResponse(data_json, content_type="application/json")



def editarCliente(request,id):
    
    edit_cliente= cliente.objects.get(id=id)
    #print(edit_carga)
    if request.method=='GET':

        cliente_form =clientesForm(instance= edit_cliente) 
        #print(contenido_form)       
    else:
        cliente_form=clientesForm(request.POST,instance=edit_cliente)
        if cliente_form.is_valid():
            cliente_form.save()
        return redirect('listarCliente')
    return render(request,'registro-cliente.html',{'form':cliente_form})

def editarTarima(request,id):
    
    edit_Tarima= Tarima.objects.get(id=id)
    #print(edit_carga)
    if request.method=='GET':

        tarima_form =TarimaForm(instance= edit_Tarima) 
        #print(contenido_form)       
    else:
        tarima_form=TarimaForm(request.POST,instance=edit_Tarima)
        if tarima_form.is_valid():
            tarima_form.save()
        return redirect('listarTarima')
    return render(request,'registro-tarima.html',{'form':tarima_form})

def eliminarCliente(request,id):    
    eliminar_cliente= cliente.objects.get(id=id)
    eliminar_cliente.delete()
    return redirect('listarCliente')

def eliminarTarima(request,id):    
    eliminar_tarima= Tarima.objects.get(id=id)
    eliminar_tarima.delete()
    return redirect('listarTarima')
    

def listarCarga(request):     
    cargas= contenido.objects.all().order_by('-id')[:5]    
    return render(request,'cargas.html',{'cargas': cargas})

def listarCarga2(request):     
    cargas= contenido2.objects.all().order_by('-id')[:5] 
    #print(cargas)
       
    return render(request,'cargas2.html',{'cargas': cargas})

def eliminarCarga2(request,id):    
    eliminar_car= contenido2.objects.get(id=id)
     # Obtiene una lista de los objetos a borrar
    contenidos = contenido2.objects.filter(id=eliminar_car.id)

    for contenido in contenidos:
        imagen1 = contenido.visual_paredes
        imagen2 = contenido.visual_piso
        imagen3= contenido.visual_techo
        imagen4= contenido.visual_tarima1
        imagen5= contenido.visual_mitad_carga
        imagen6= contenido.visual_fin_carga
        imagen7= contenido.visual_cerrado_unidad

    ruta_imagen1 =imagen_media12+ str(imagen1)
    ruta_imagen2 =imagen_media12+ str(imagen2)
    ruta_imagen3 =imagen_media12+ str(imagen3)
    ruta_imagen4 =imagen_media12+ str(imagen4)
    ruta_imagen5 =imagen_media12+ str(imagen5)
    ruta_imagen6 =imagen_media12+ str(imagen6)
    ruta_imagen7 =imagen_media12+ str(imagen7)

    
    # Lista de archivos a eliminar
    archivos = [ruta_imagen1, ruta_imagen2, ruta_imagen3, ruta_imagen4, ruta_imagen5, ruta_imagen6, ruta_imagen7]
    # Bucle for para eliminar cada archivo
    import os
    for archivo in archivos:
        os.remove(archivo) 
    eliminar_car.delete()
    return redirect('listarCarga2')


#lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

def editarCarga(request,id):
    
    edit_carga= contenido.objects.get(id=id)

    imagen1 = edit_carga.visual_paredes
    imagen2 = edit_carga.visual_piso
    imagen3= edit_carga.visual_techo
    imagen4= edit_carga.visual_tarima1
    imagen5= edit_carga.visual_mitad_carga
    imagen6= edit_carga.visual_fin_carga
    imagen7= edit_carga.visual_cerrado_unidad

    ruta_imagen1 =imagen_media12+ str(imagen1)    
    ruta_imagen2 =imagen_media12+ str(imagen2)
    ruta_imagen3 =imagen_media12+ str(imagen3)
    ruta_imagen4 =imagen_media12+ str(imagen4)
    ruta_imagen5 =imagen_media12+ str(imagen5)
    ruta_imagen6 =imagen_media12+ str(imagen6)
    ruta_imagen7 =imagen_media12+ str(imagen7)
    
    if request.method=='GET':

        contenido_form =contenidoForm(instance= edit_carga) 
             
    else:
        contenido_form=contenidoForm(request.POST,request.FILES,instance=edit_carga)

        if contenido_form.is_valid():
            contenido_form.save() 

        edit_carga= contenido.objects.get(id=id)
       
        imagen11 = edit_carga.visual_paredes
        imagen22 = edit_carga.visual_piso
        imagen33= edit_carga.visual_techo
        imagen44= edit_carga.visual_tarima1
        imagen55= edit_carga.visual_mitad_carga
        imagen66= edit_carga.visual_fin_carga
        imagen77= edit_carga.visual_cerrado_unidad

        ruta_imagen11 =imagen_media12+ str(imagen11)        
        ruta_imagen22 =imagen_media12+ str(imagen22)
        ruta_imagen33 =imagen_media12+ str(imagen33)
        ruta_imagen44 =imagen_media12+ str(imagen44)
        ruta_imagen55 =imagen_media12+ str(imagen55)
        ruta_imagen66 =imagen_media12+ str(imagen66)
        ruta_imagen77 =imagen_media12+ str(imagen77)
        import os
        if ruta_imagen1 !=ruta_imagen11:
            os.remove(ruta_imagen1)
            
        elif ruta_imagen2 !=ruta_imagen22:
            os.remove(ruta_imagen2)
            
        elif ruta_imagen3 !=ruta_imagen33:
            os.remove(ruta_imagen3)

        elif ruta_imagen4 !=ruta_imagen44:
            os.remove(ruta_imagen4)

        elif ruta_imagen5 !=ruta_imagen55:
            os.remove(ruta_imagen5)

        elif ruta_imagen6 !=ruta_imagen66:
            os.remove(ruta_imagen6)

        elif ruta_imagen7 !=ruta_imagen77:
            os.remove(ruta_imagen7)

       
            
        return redirect('listarCarga')
    return render(request,'registro-carga-editar.html',{'form':contenido_form})




def exportar_cargas_pdf(request,id):
    cargas = contenido2.objects.get(id=id)
    object_id = getattr(cargas, "id")
    
    
   # Usamos filter en vez de get para obtener un QuerySet
    productos = Tarima2.objects.filter(contenido2_id=object_id)
    
    # Creamos una lista con los valores de los campos producto y lote
    productos_lotes = productos.values_list('producto_tarima', 'lote_tarima', flat=False)

    # Creamos un contador con los valores y sus frecuencias
    resumen = Counter(productos_lotes)

    # Imprimimos el resultado
    datos = resumen

    hora_registro_str = cargas.hora_registro.strftime("%H:%M:%S")

    #obteniendo datos de tarima2

    productos1 = Tarima2.objects.filter(contenido2_id=object_id).values_list(
    "numero_tarima", "producto_tarima", "lote_tarima", "camas_tarima", "paquetes_tarima", "latas_tarima", "charolas_tarima", "emplayado_tarima", "observaciones_tarima"
    )
    #Convertir el QuerySet en una lista
    productos1 = list(productos1)
    datos1 = productos1
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=cargas.pdf"
    buffer=BytesIO()
    c = canvas.Canvas(buffer,pagesize= A4)
    #Header 
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)

    logo = finders.find('agama/logo.jpg')
    if logo:
        c.drawImage(logo, 30, 745, width=100, height=80) 
    c.rect(30, 750, width=100, height=60)
    c.line(130,750,550,750)
    c.line(130,810,550,810)
    c.line(130,793,550,793)
    c.line(550, 810, 550, 750) # x1, y1, x2, y2
    c.line(470, 810, 470, 750) # x1, y1, x2, y2
    c.line(470,776,550,776)
    c.line(470,760,550,760)
    #c.line(130,759,550,759)
    c.rect(30, 725, width=520, height=20)
    c.line(130, 745, 130, 725) # x1, y1, x2, y2
    c.line(260, 745, 260, 725) # x1, y1, x2, y2
    c.line(390, 745, 390, 725) # x1, y1, x2, y2
    #datos del cliente 
    c.rect(30, 700, width=520, height=20)
    c.rect(30, 635, width=520, height=60)
    c.line(30,675,550,675)
    c.line(30,655,550,655)
    c.line(130, 695, 130, 635) # x1, y1, x2, y2   
    #datos del transporte 
    c.rect(30, 610, width=520, height=20)
    c.rect(30, 525, width=520, height=80)
    c.line(30,585,550,585)
    c.line(30,565,550,565)
    c.line(30,545,550,545)
    c.line(135, 605, 135, 545) # x1, y1, x2, y2
    c.line(265, 605, 265, 525) # x1, y1, x2, y2
    c.line(395, 605, 395, 525) # x1, y1, x2, y2
    #condiciones visuales de la unidad
    c.rect(30, 500, width=520, height=20)  
    c.rect(30, 345, width=520, height=20)
    c.line(135, 365, 135, 345) # x1, y1, x2, y2
    c.line(265, 365, 265, 345) # x1, y1, x2, y2
    c.line(395, 365, 395, 345) # x1, y1, x2, y2 
    #condiciones visuales del producto de entrega
    c.rect(30, 320, width=520, height=20)
    c.rect(30, 175, width=520, height=20)
    c.line(135, 195, 135, 175) # x1, y1, x2, y2
    c.line(265, 195, 265, 175) # x1, y1, x2, y2
    c.line(395, 195, 395, 175) # x1, y1, x2, y2 
    #producto entregado
    c.rect(30, 95, width=520, height=80)
    c.line(30,150,550,150) 
    #firmas
    c.line(30,60,190,60) 
    c.line(200,60,360,60) 
    c.line(370,60,550,60) 
    

    c.setFont('Helvetica',8)    
    c.drawString(150, 795, "Departamento: Control de Calidad")
    c.drawString(35, 730, "Fecha de entrega:")
    c.drawString(145, 730, cargas.fecha_registro.strftime("%d/%m/%Y")+"      "+hora_registro_str)
    c.drawString(300, 730, "Numero de reporte:")
    c.drawString(460, 730, str(object_id))
    #datos del cliente 
    c.drawString(250, 705, "DATOS DEL CLIENTE")
    c.drawString(35, 679, "Nombre del cliente:")
    c.drawString(140, 679, cargas.nombre_cliente)
    c.drawString(35, 659, "Direccion fiscal:")
    c.drawString(140, 659, cargas.direccion_fiscal)
    c.drawString(35, 639, "Contacto:")
    c.drawString(140, 639, cargas.contacto_dir)
    #datos del transporte 
    c.drawString(235, 615, "DATOS DEL TRANSPORTE")
    c.drawString(35, 589, "Empresa transportadora:")
    c.drawString(140, 589, cargas.empresa_transportadora)
    c.drawString(35, 569, "Nombre del transportista:")
    c.drawString(140, 569, cargas.nombre_transportista)
    c.drawString(35, 549, "No. licencia(operador):")
    c.drawString(140, 549, cargas.licencia)
    c.drawString(35, 529, "Certificado de fumigacion:"+"  "+"si"+"     "+"no"+"    "+"  "+"Numero:" )
    c.drawString(202, 529, cargas.certificado_fumigacion)

    c.drawString(270, 589, "Tracto camion:")
    c.drawString(400, 589, cargas.tracto_camion)
    c.drawString(270, 569, "Placas de la unidad:")
    c.drawString(400, 569, cargas.placas_unidad)
    c.drawString(270, 549, "Placas de la caja:")
    c.drawString(400, 549, cargas.placas_caja)
    c.drawString(270, 529, "No. Caja")
    c.drawString(400, 529, cargas.numero_caja)
    #condiciones visuales de la unidad
    c.drawString(220, 505, "Condiciones visuales de la unidad")
    c.drawString(60, 375, "(Paredes)")
    c.drawImage(cargas.visual_paredes.path, 30, 390, width=100, height=100)
    c.drawString(280, 375, "(Piso)")
    c.drawImage(cargas.visual_piso.path, 245, 390, width=100, height=100)
    c.drawString(480, 375, "(Techo)")
    c.drawImage(cargas.visual_techo.path, 445, 390, width=100, height=100)
    c.drawString(40, 349, "Hora de llegada:")
    c.drawString(150, 349, cargas.hora_llegada)
    c.drawString(270, 349, "Hora inicio de carga:")
    c.drawString(400, 349, cargas.hora_inicio_carga)
    #condiciones visuales del producto de entrega
    c.drawString(200, 324, "Condiciones visuales del producto de entrga")
    c.drawString(60, 200, "(Primer tarima)")
    c.drawImage(cargas.visual_paredes.path, 30, 215, width=100, height=100)
    c.drawString(180, 200, "(Mitad de carga)")
    c.drawImage(cargas.visual_piso.path, 165, 215, width=100, height=100)
    c.drawString(330, 200, "(Fin de carga)")
    c.drawImage(cargas.visual_techo.path, 300, 215, width=100, height=100)
    c.drawString(450, 200, "(Cerrado de la unidad)")
    c.drawImage(cargas.visual_techo.path, 435, 215, width=100, height=100)
    c.drawString(40, 180, "Hora finde carga:")
    c.drawString(150, 180, cargas.hora_fin_carga)
    c.drawString(270, 180, "Hora de salida:")
    c.drawString(400, 180, cargas.hora_salida)
    #producto entregado
    c.drawString(240, 155, "PRODUCTO ENTREGADO")    
    c.drawString(32, 134, str(datos))
    c.drawString(32, 126, "Dichos productos se entregan en optimas condiciones.Correctamente estibado,emplayado y sin producto que presente,golpes,fugas o derrames.")
    c.drawString(32, 118, "Por lo que una vez embarcado EMBOTELLADORA AGA S.A DEC.V NO SE HACE RESPONSABLE DEL MAL MANEJO DE ESTE PRODUCTO. ")
    c.drawString(32, 110, "Cumpliendo al maximos porcentaje de calidad y servicio en la entrega del producto y con nuestros clientes")
    #firmas
    c.drawString(65, 52, "Revisa y reporta (Analista)")
    c.drawString(85, 44, "Nombre y firma")
    c.drawString(235, 52, "Responsable de la unidad")
    c.drawString(250, 44, "Nombre y firma")
    c.drawString(390, 52, "Verifica informacion(Control de calidad)")
    c.drawString(430, 44, "Nombre y firma")  
    

    
    #c.rect(150, 790, width=250, height=10)

    c.setFont('Helvetica-Bold',10)    
    c.drawString(150, 780, "Inspeccion y liberacion de entrega de producto de maquila")
    #c.rect(150, 775, width=250, height=10)
   
   
    
    c.setFont('Helvetica-Bold',8)
    c.drawString(480, 795, "D-K-LL-AC-12")

    
    c.drawString(480, 780, "Revision 01")

    
    c.drawString(480, 765, "18-OCT-21")

    
    c.drawString(480, 750, "Pagina 1-1") 

#segunda hoja---------------------------------------------------------------------------------------
    c.showPage()

    c.setLineWidth(.3)
    c.setFont('Helvetica',22)

    logo = finders.find('agama/logo.jpg')
    if logo:
        c.drawImage(logo, 30, 745, width=100, height=80) 
    c.rect(30, 750, width=100, height=60)
    c.line(130,750,550,750)
    c.line(130,810,550,810)
    c.line(130,793,550,793)
    c.line(550, 810, 550, 750) # x1, y1, x2, y2
    c.line(470, 810, 470, 750) # x1, y1, x2, y2
    c.line(470,776,550,776)
    c.line(470,760,550,760)
    #datos generales
    c.rect(30, 725, width=520, height=20)    
    c.rect(30, 620, width=520, height=100)
    c.line(30,700,550,700)
    c.line(30,680,550,680)
    c.line(30,660,550,660)
    c.line(30,640,550,640)
    c.line(135, 720, 135, 620) # x1, y1, x2, y2
    c.line(265, 720, 265, 620) # x1, y1, x2, y2
    c.line(395, 720, 395, 620) # x1, y1, x2, y2
    #puntos de revision 
    c.rect(30, 595, width=520, height=20)
    c.rect(30, 490, width=520, height=100)
    c.line(30,570,550,570)
    c.line(30,550,550,550)
    c.line(30,530,550,530)
    c.line(30,510,550,510)
    c.line(170, 570, 170, 490) # x1, y1, x2, y2
    c.line(200, 590, 200, 490) # x1, y1, x2, y2
    c.line(340, 570, 340, 490) # x1, y1, x2, y2
    c.line(370, 590, 370, 490) # x1, y1, x2, y2
    c.line(520, 570, 520, 490) # x1, y1, x2, y2
    c.setFont('Helvetica',8) 
    c.drawString(35, 574, "PISOS EN BUEN ESTADO" )
    c.drawString(35, 554, "SIN HOYOS")     
    c.drawString(175, 554, cargas.sin_hoyos)
    c.drawString(35, 534, "SIN PARCHES Y/O DESNIVELES")     
    c.drawString(175, 534, cargas.sin_parches)
    c.drawString(35, 514, "SIN OBJETOS SALIENTES")     
    c.drawString(175, 514, cargas.sin_salientes)
    c.drawString(35, 494, "SIN LAMINAS SUELTAS")     
    c.drawString(175, 494, cargas.sin_laminas)

    c.drawString(230, 574, "PUERTAS EN BUEN ESTADO" )
    c.drawString(205, 554, "EMPAQUES EN BUEN ESTADO")     
    c.drawString(345, 554, cargas.puertas_empaques)
    c.drawString(205, 534, "CIERRE HERMETICO")     
    c.drawString(345, 534, cargas.puertas_hermetico)
    c.drawString(205, 514, "SIN OBJETOS SALIENTES")     
    c.drawString(345, 514, cargas.puertas_salientes)
    c.drawString(205, 494, "SIN LAMINAS SUELTAS")     
    c.drawString(345, 494, cargas.puertas_laminas)

    c.drawString(390, 574, "CONDICIONES DE HIGIENE" )
    c.drawString(375, 554, "LIMPIOS")     
    c.drawString(525, 554, cargas.higiene_limpios)
    c.drawString(375, 534, "SIN OLORES")     
    c.drawString(525, 534, cargas.higiene_olores)
    c.drawString(375, 514, "SIN PLAGAS")     
    c.drawString(525, 514, cargas.higiene_plagas)

    c.rect(30, 365, width=520, height=120)
    c.line(30,465,550,465)
    c.line(30,445,550,445)
    c.line(30,425,550,425)
    c.line(30,405,550,405)
    c.line(30,385,550,385)
    c.line(170, 465, 170, 365) # x1, y1, x2, y2
    c.line(200, 485, 200, 365) # x1, y1, x2, y2
    c.line(340, 465, 340, 365) # x1, y1, x2, y2
    c.line(370, 485, 370, 365) # x1, y1, x2, y2
    c.line(520, 465, 520, 365) # x1, y1, x2, y2
    c.setFont('Helvetica',8) 
    c.drawString(35, 470, "CONDICIONES EXTERNAS" )
    c.drawString(35, 450, "LLANTAS UNIDAD")     
    c.drawString(175, 450, cargas.sin_hoyos)
    c.drawString(35, 430, "LLANTAS REFACCION")     
    c.drawString(175, 430, cargas.sin_parches)
    c.drawString(35, 410, "PATINES DE LA CAJA")
    c.drawString(175, 410, cargas.sin_salientes)
    c.drawString(35, 390, "LUCES COMPLETAS")     
    c.drawString(175, 390, cargas.sin_laminas)
    c.drawString(35, 370, "TANQUE DE COMBUSTIBLE")     
    c.drawString(175, 370, cargas.sin_laminas)

    c.drawString(230, 470, "PAREDES EN BUEN ESTADO" )
    c.drawString(205, 450, "SIN HOYOS")     
    c.drawString(345, 450, cargas.puertas_empaques)
    c.drawString(205, 430, "SIN PARCHES Y/O DESNIVELES")     
    c.drawString(345, 430, cargas.puertas_hermetico)
    c.drawString(205, 410, "SIN OBJETOS SALIENTES")     
    c.drawString(345, 410, cargas.puertas_salientes)
    c.drawString(205, 390, "SIN LAMINAS SUELTAS")     
    c.drawString(345, 390, cargas.puertas_laminas)

    c.drawString(390, 470, "TECHOS EN BUEN ESTADO" )
    c.drawString(375, 450, "SIN HOYOS(GOTERAS)")     
    c.drawString(525, 450, cargas.higiene_limpios)
    c.drawString(375, 430, "SIN OBJETOS SALIENTES")     
    c.drawString(525, 430, cargas.higiene_olores)
    c.drawString(375, 410, "SIN LAMINAS SUELTAS")     
    c.drawString(525, 410, cargas.higiene_plagas)

    #tabla de criterios        
    c.rect(30, 260, width=110, height=100)
    c.line(30,340,140,340)
    c.line(30,320,140,320)
    c.line(30,300,140,300)
    c.line(30,280,140,280)
    c.line(100, 360, 100, 260) # x1, y1, x2, y2
    c.setFont('Helvetica',8)
    c.drawString(35, 345, "ACEPTADO")
    c.drawString(35, 325, "RECHAZADO")
    c.drawString(35, 305, "NO APLICA")
    c.drawString(35, 285, "CRITICA")
    c.drawString(35, 265, "NECESARIA")

    c.drawString(105, 345, "A")
    c.drawString(105, 325, "X")
    c.drawString(105, 305, "-")
    c.drawString(105, 285, "C")
    c.drawString(105, 265, "N")

    c.rect(180, 300, width=150, height=60)
    c.line(180,340,330,340)
    c.line(180,320,330,320)
    c.setFont('Helvetica',8)
    c.drawString(185, 345, "CRITERIOS DE ACEPTACION ")
    c.drawString(185, 325, "CRITICOS"+"                    "+"0")
    c.drawString(185, 305, "NECESARIOS"+"               "+"3 MAXIMOS")

    #dictamen de la unidad
    c.rect(30, 235, width=520, height=20)
    c.rect(100, 210, width=30, height=20)
    c.rect(280, 210, width=30, height=20)
    c.rect(510, 210, width=30, height=20)
    c.setFont('Helvetica',8)
    c.drawString(225, 240, "DICTAMEN DE LA UNIDAD DE TRASNPORTE")
    c.drawString(30, 215, "RECHAZADO")
    c.drawString(200, 215, "ACEPTADO")
    c.drawString(380, 215, "RECHAZADO CON REPORTE")
    c.rect(30, 145, width=520, height=60)
    c.setFont('Helvetica',8)
    c.drawString(35, 190, "OBSERVACIONES")
    #firmas
    c.line(30,60,190,60) 
    c.line(200,60,360,60) 
    c.line(370,60,550,60)
    c.drawString(65, 52, "Revisa y reporta (Analista)")
    c.drawString(85, 44, "Nombre y firma")
    c.drawString(235, 52, "Responsable de la unidad")
    c.drawString(250, 44, "Nombre y firma")
    c.drawString(390, 52, "Verifica informacion(Control de calidad)")
    c.drawString(430, 44, "Nombre y firma")     
    
    c.setFont('Helvetica-Bold',10)    
    c.drawString(150, 780, "Inspeccion y liberacion de entrega de producto de maquila")
    c.setFont('Helvetica',8)    
    c.drawString(150, 795, "Departamento: Control de Calidad")
    #datos generales
    c.drawString(240, 734, "DATOS GENERALES")     
    c.drawString(35, 629, "Numero de reporte")
    c.drawString(140, 629, str(object_id))
    c.drawString(35, 649, "Empresa transportadora")
    c.drawString(140, 649, cargas.empresa_transportadora)
    c.drawString(35, 669, "Nombre del transportista")
    c.drawString(140, 669, cargas.nombre_transportista)
    c.drawString(35, 689, "Placas tracto" )
    c.drawString(140, 689, cargas.placas_unidad)
    c.drawString(35, 709, "Placas de la caja" )
    c.drawString(140, 709, cargas.placas_caja)

    c.drawString(270, 629, "Fecha")
    c.drawString(400, 629, cargas.fecha_registro.strftime("%d/%m/%Y")+"      "+hora_registro_str)
    #c.drawString(270, 649, "")
    #c.drawString(400, 649, cargas.placas_unidad)
    c.drawString(270, 669, "Tracto")
    c.drawString(400, 669, cargas.tracto_camion)
    c.drawString(270, 689, "Certificado fumigacion")
    c.drawString(400, 689, cargas.certificado_fumigacion)
    c.drawString(270, 709, "No. Caja")
    c.drawString(400, 709, cargas.numero_caja)
    #puntos de revision
    c.drawString(235, 600, "PUNTOS DE REVISION")  

   
   
    
    c.setFont('Helvetica-Bold',8)
    c.drawString(480, 795, "D-K-LL-AC-12")

    
    c.drawString(480, 780, "Revision 01")

    
    c.drawString(480, 765, "18-OCT-21")

    
    c.drawString(480, 750, "Pagina 1-1") 

    #TERCERA PAGINA-----------------------------------------------------------------------------------------------------------------------
    
    c.showPage()
    # Dibujar el contenido de la segunda hoja
    c.setPageSize(landscape(A4))
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)

    logo = finders.find('agama/logo.jpg')
    if logo:
        c.drawImage(logo, 30, 495, width=100, height=80) 
    c.rect(30, 500, width=100, height=80)
    c.line(130,580,800,580)
    c.line(130,500,800,500)
    c.line(130,560,800,560)
    c.line(800, 580, 800, 500) # x1, y1, x2, y2
    c.line(720, 580, 720, 500) # x1, y1, x2, y2
    c.line(720,540,800,540)
    c.line(720,520,800,520)

    c.setFont('Helvetica-Bold',8)
    c.drawString(150, 565, "Departamento: Control de Calidad")
    c.drawString(725, 565, "D-K-LL-AC-12")    
    c.drawString(725, 545, "Revision 01")    
    c.drawString(725, 525, "18-OCT-21")    
    c.drawString(725, 505, "Pagina 1-1") 
    c.setFont('Helvetica-Bold',10)    
    c.drawString(290, 545, "Inspeccion y liberacion de entrega de producto de maquila")

    

    c.rect(30, 475, width=770, height=20)
    c.line(195, 495, 195, 475) # x1, y1, x2, y2
    c.line(390, 495, 390, 475) # x1, y1, x2, y2
    c.line(586, 495, 586, 475) # x1, y1, x2, y2
    c.setFont('Helvetica-Bold',8)
    c.drawString(35, 480, "Numero de embarque:" )
    c.drawString(200, 480, str(object_id))
    c.drawString(395, 480, "Fecha de embarque:")
    c.drawString(605, 480, cargas.fecha_registro.strftime("%d/%m/%Y")+"      "+hora_registro_str)
    encabezados=["TARIMA", "PRODUCTO", "NUMERO DE LOTE ", "No. cama", "No. paquetes", "Lata", "Charolas", "Emplayado", "Observaciones"]
    data = [encabezados]+datos1
    

    # Crear un objeto Table con los datos y el tamaño de las celdas
    #table = Table(data, colWidths=[50, 180, 100,50,60,50,50,55,180])
    table = Table(data, colWidths=[50, 180, 100,50,60,50,50,55,178], rowHeights=[0.7*cm]+[0.46*cm]*(len(data)-1))

    # Aplicar un estilo a la tabla para cambiar el color de fondo, el grosor de las líneas y la alineación del texto
    table.setStyle(TableStyle([
    # Color de fondo de la primera fila
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    # Grosor de las líneas horizontales
    ("LINEBELOW", (0, 0), (-1, -1), 1, colors.black),
    # Grosor de las líneas verticales
    ("LINEAFTER", (0, 0), (-1, -1), 1, colors.black),
    # Alineación del texto al centro
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    # Tamaño de la fuente de la primera fila
    ("FONTSIZE", (0, 0), (-1, 0), 7),
    # Tamaño de la fuente del resto de celdas
    ("FONTSIZE", (0, 1), (-1, -1), 7),
    # Alineación vertical del texto en la parte de abajo
    #("VALIGN", (0, 1), (-2, -2), "BOTTOM")
    ]))

   

    # Dibujar la tabla en el canvas usando el espacio como referencia
    table.wrapOn(c, 0, 0)
    table.drawOn(c, 30, 105)
    c.setFont('Helvetica-Bold',8)
    c.drawString(30, 95, "NOTAS:" )
    c.setFont('Helvetica',8)
    c.drawString(60, 95, "LAS ESPECIFICACIONES DE CUMPLIMIENTO SON ENVIADAS POR EL CLIENTE. MISMAS QUE SON EJECUTADAS POR EL DEPARTAMENTO DE CONTROL DE CALIDAD DE LA PLANTA." )
    c.drawString(30, 85, "LA ENTREGA SE REALIZA EN PRESENCIA DEL TRANSPORTISTA. QUIEN DECLARA EN QUE CONDICIONES SE ENTREGA EL PRODUCTO,Y SI POR ALGUNA RAZON EL PRODUCTO PRESENTA ALGUN")
    c.drawString(30, 75, "DAÑO, DEBERA SER,REGISTRADO Y SOPORTADO CON EVIDENCIA(informacion,fotografia.etc).")
    c.drawString(30, 65, "RECIBI:")
    c.drawString(60, 65, str(datos))
    c.drawString(30, 50, "NOMBRE:")
    c.line(70,50,250,50)
    c.drawString(250, 50, "FIRMA")
    c.line(280,50,450,50)
    c.drawString(455, 50, "CONDICIONES")
    c.line(520,50,800,50)

    #firmas
    c.line(30,29,190,29) 
    c.line(320,29,480,29) 
    c.line(610,29,800,29)
    c.drawString(65, 20, "Revisa y reporta (Analista)")
    c.drawString(85, 10, "Nombre y firma")
    c.drawString(350, 20, "Responsable de la unidad")
    c.drawString(380, 10, "Nombre y firma")
    c.drawString(620, 20, "Verifica informacion(Control de calidad)")
    c.drawString(660, 10, "Nombre y firma")     
    
    c.setFont('Helvetica-Bold',10)    
    c.drawString(150, 780, "Inspeccion y liberacion de entrega de producto de maquila")
    c.setFont('Helvetica',8)    
    c.drawString(150, 795, "Departamento: Control de Calidad")

  
   
    c.save()
    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

