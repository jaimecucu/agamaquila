from email import utils
from io import BytesIO
from mmap import PAGESIZE
import reportlab
from django.shortcuts import render,redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter
from reportlab.lib import utils
from  django.templatetags.static import  static
import subprocess
from .forms import contenidoForm,clientesForm#,transporteForm,transporte1Form,productoForm,producto1Form,visualForm,visual1Form,visual_productoForm,visual_producto1Form
from .models import contenido,cliente
from django.conf import settings
import  os
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.views.generic import View
from django.http import JsonResponse
import json







#from django.template.loader import render_to_string
# Create your views here.

def menuaga(request):  
    return render(request,'base.html')

def registroCliente(request):  
    data = {
        'form':clientesForm()
        
    }

    if request.method == 'POST':
        contenido_form=clientesForm(request.POST)
        nom = request.POST['nombre_cliente']

        #contenido_form=clientesForm(request.POST)
        comprocliete=cliente.objects.filter(nombre_cliente=nom)
        if comprocliete:
             messages.error(request, "El cliente ya existe.")        
        

        else: #contenido_form.is_valid()
            contenido_form.save() 
            messages.success(request, "Operacion exitosa.")           
        #messages.success(request, "Tu accion fue exitosa.")    
       
            
    return render(request,'registro-cliente.html',data)



def embarque(request):
   

    data = {
        'form':contenidoForm()
        
    }

    if request.method == 'POST':

        contenido_form=contenidoForm(request.POST,request.FILES)
        print(contenido_form)

        if contenido_form.is_valid():
            contenido_form.save()
            data["mensaje"] = "datos guardados"
            
        else:
            data["form"]=contenido_form
    return render(request,'registro.html',data)

def listarCliente(request):     
    clientes= cliente.objects.all().order_by('-id')[:5]    
    return render(request,'clientes-lista.html',{'clientes': clientes})

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
  print(id)
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

def eliminarCliente(request,id):    
    eliminar_cliente= cliente.objects.get(id=id)
    eliminar_cliente.delete()
    return redirect('listarCliente')
    

def listarCarga(request):     
    cargas= contenido.objects.all().order_by('-id')[:5]    
    return render(request,'cargas.html',{'cargas': cargas})

def editarCarga(request,id):
    
    edit_carga= contenido.objects.get(id=id)
    #print(edit_carga)
    if request.method=='GET':

        contenido_form =contenidoForm(instance= edit_carga) 
        #print(contenido_form)       
    else:
        contenido_form=contenidoForm(request.POST,request.FILES,instance=edit_carga)
        if contenido_form.is_valid():
            contenido_form.save()
        return redirect('listarCarga')
    return render(request,'registro.html',{'form':contenido_form})




def exportar_cargas_pdf(request,id):
    cargas = contenido.objects.get(id=id)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=cargas.pdf"
    buffer=BytesIO()
    c = canvas.Canvas(buffer,pagesize= A4)
    #Header 
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)

    logo = finders.find('agama/logo.jpg')
    if logo:
        c.drawImage(logo, 10, 750, width=100, height=80) 
    c.rect(10, 750, width=100, height=80)
    

    c.setFont('Helvetica',8)    
    c.drawString(150, 795, "Departamento: Control de Calidad")
    #c.rect(150, 790, width=250, height=10)

    c.setFont('Helvetica-Bold',10)    
    c.drawString(150, 780, "Inspeccion y liberacion de entrega de producto de maquila")
    #c.rect(150, 775, width=250, height=10)
   
   
    
    c.setFont('Helvetica-Bold',8)
    c.drawString(480, 795, "D-K-LL-AC-12")

    
    c.drawString(480, 780, "Revision 01")

    
    c.drawString(480, 765, "18-OCT-21")

    
    c.drawString(480, 750, "Pagina 1-1") 

    c.drawString(30, 700, "Cliente:"+cargas.nombre_cliente)
    c.drawString(30, 680, "Imagen paredes")
    c.drawImage(cargas.visual_paredes.path, 30, 570, width=100, height=100)
    
    
   
    c.save()
    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

