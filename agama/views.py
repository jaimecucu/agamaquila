from django.shortcuts import render
from .forms import contenidoForm#,transporteForm,transporte1Form,productoForm,producto1Form,visualForm,visual1Form,visual_productoForm,visual_producto1Form

# Create your views here.

def menuaga(request):  
    return render(request,'base.html')

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

