from django import forms
from .models import contenido,cliente,Tarima,contenido2,Tarima2
from django.forms import ModelChoiceField



class contenido_terminarForm(forms.ModelForm):
    class Meta:
        model =contenido
        exclude = ('nombre_cliente', 'direccion_fiscal', 'contacto_dir', 'empresa_transportadora', 'nombre_transportista', 'licencia', 'certificado_fumigacion', 'tracto_camion', 'placas_unidad', 'placas_caja', 'numero_caja','sin_hoyos', 'sin_parches', 'sin_salientes', 'sin_laminas', 'puertas_empaques', 'puertas_hermetico', 'puertas_salientes', 'puertas_laminas', 'higiene_limpios', 'higiene_olores', 'higiene_plagas', 'paredes_hoyos', 'paredes_parches', 'paredes_salientes', 'paredes_laminas', 'techos_hoyos', 'techos_salientes', 'techos_laminas','externas_llantas', 'externas_refaccion', 'externas_patines', 'externas_luces', 'externas_tanque', 'producto', 'cantidad_charolas', 'numero_lote', 'cantidad_tarimas','visual_paredes', 'visual_piso', 'visual_techo', 'hora_llegada', 'hora_inicio_carga') # Excluimos estos campos
       
        
        fields = '__all__' 
        labels = {
            'hora_fin_carga':'Hora fin de carga:',            
            'hora_salida':'Hora de salida:',
            #eeeeeeeeeee
            'visual_tarima1':'Primer tarima:',
            'visual_mitad_carga' :'Mitad de carga:',
            'visual_fin_carga':'Fin de carga:',
            'visual_cerrado_unidad':'Cerrado de la unidad:', 
                    
            }   
        widgets = {
              #dddddddddd
            'hora_fin_carga': forms.TextInput(attrs={'class':'form-control'}),            
            'hora_salida': forms.TextInput(attrs={'class':'form-control'}), 
            #tttttttttttttt
            'visual_tarima1': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_tarima1'}),
            'visual_mitad_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_mitad_carga'}),
            'visual_fin_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_fin_carga'}),
            'visual_cerrado_unidad': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_cerrado_unidad'}),      
            
            
        }




class contenidoForm(forms.ModelForm):
    class Meta:
        model =contenido
        exclude = ('hora_salida', 'hora_fin_carga','visual_tarima1','visual_mitad_carga','visual_fin_carga','visual_cerrado_unidad') # Excluimos estos campos
        
        fields = '__all__' 
        labels = {
            'nombre_cliente':'Nombre del cliente:',
            'direccion_fiscal':'Direccion fiscal:',
            'contacto_dir':'Contacto:',
            #fffffffff
            'empresa_transportadora':'Empresa transportadora:',
            'nombre_transportista':'Nombre del transportista:',
            'licencia':'No de licencia:',
            'certificado_fumigacion':'Certificado de fumigacion:',
            #sssss
            'tracto_camion':'Tracto camion:',
            'placas_unidad':'Placas de la unidad:',
            'placas_caja':'Placas de la caja:',
            'numero_caja':'No de caja:', 

            #puntos de revision 
            'sin_hoyos':'Sin hoyos:',
            'sin_parches':'Sin parches y/o desniveles:',
            'sin_salientes':'Sin objetos salientes:',
            'sin_laminas':'Sin laminas sueltas:',

            #puertas en buen estado

            'puertas_empaques':'Empaques en buen estado:',
            'puertas_hermetico':'Cierre hermetico:',
            'puertas_salientes':'Sin objetos salientes:',
            'puertas_laminas':'Sin laminas sueltas:',

            #condiciones de higiene

            'higiene_limpios':'Limpios:',
            'higiene_olores':'Sin olores:',
            'higiene_plagas':'Sin plagas:',

            #paredes en buen estado

            'paredes_hoyos':'Sin hoyos:',
            'paredes_parches':'Sin parches y/o desniveles:',
            'paredes_salientes':'Sin objetos salientes:',
            'paredes_laminas':'Sin laminas sueltas:',

            #techos en buen estado

            'techos_hoyos':'Sin hoyos(goteras):',
            'techos_salientes':'Sin objetos salientes:',
            'techos_laminas':'Sin laminas sueltas:',

            #condiciones externas

            'externas_llantas':'LLantas unidad:',
            'externas_refaccion':'LLanta refaccion:',
            'externas_patines':'Patines de la caja:',
            'externas_luces':'Luces completas:',
            'externas_tanque':'Tanque de combustible:',
    

            #ffffffffff
            'producto':'Producto:', 
            'cantidad_charolas':'Cantidad total de charolas:',
            #fffffffffffff
            'numero_lote':'Numero de lote:',
            'cantidad_tarimas':'Cantidad total de tarimas:',
            #dddddddd 
            'visual_paredes':'(Paredes)',
            'visual_piso':'(Piso)',
            'visual_techo':'(Techo)', 
            #dddddd
            'hora_llegada':'Hora de llegada:',
            #'hora_salida':'Hora de salida:', 
            #eeeeeeeeeee
            #'visual_tarima1':'Primer tarima:',
            #'visual_mitad_carga' :'Mitad de carga:',
            #'visual_fin_carga':'Fin de carga:',
            #'visual_cerrado_unidad':'Cerrado de la unidad:',
            #gggggggg
            'hora_inicio_carga':'Hora inicio de carga:',
            #'hora_fin_carga':'Hora fin de carga:',                  
                    
            }      
        
        widgets = {
           
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','id':"nombre"}),           
            'direccion_fiscal': forms.TextInput(attrs={'class':'form-control','id':"direccion"}),
            'contacto_dir': forms.TextInput(attrs={'class':'form-control','id':"contacto"}),
            #ddddddd
            'empresa_transportadora': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_transportista': forms.TextInput(attrs={'class':'form-control'}),
            'licencia': forms.TextInput(attrs={'class':'form-control'}),
            'certificado_fumigacion': forms.TextInput(attrs={'class':'form-control'}),
            #fffffff
            'tracto_camion': forms.TextInput(attrs={'class':'form-control'}),
            'placas_unidad': forms.TextInput(attrs={'class':'form-control'}),
            'placas_caja': forms.TextInput(attrs={'class':'form-control'}),
            'numero_caja': forms.TextInput(attrs={'class':'form-control'}),

            #puntos de revision 
            #pisos en buen estado
            'sin_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_parches': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #puertas en buen estado

            'puertas_empaques': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_hermetico': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #condiciones de higiene

            'higiene_limpios': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'higiene_olores': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'higiene_plagas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #paredes en buen estado

            'paredes_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_parches': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

             #techos en buen estado

            'techos_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'techos_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'techos_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

             #condiciones externas

             'externas_llantas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_refaccion': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_patines': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_luces': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_tanque': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
           
            #dddddddddd
            'producto': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_charolas': forms.TextInput(attrs={'class':'form-control'}),
            #kkkkkkkkk
            'numero_lote': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_tarimas': forms.TextInput(attrs={'class':'form-control'}),
            #tttttttttttttt
            'visual_paredes': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_paredes'}),
            'visual_piso': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_piso'}),
            'visual_techo': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_techo'}),
            #dddddddddddd
            'hora_llegada': forms.TextInput(attrs={'class':'form-control'}),
            'hora_salida': forms.TextInput(attrs={'class':'form-control'}),
            #tttttttttttttt
            #'visual_tarima1': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_tarima1'}),
            #'visual_mitad_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_mitad_carga'}),
            #'visual_fin_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_fin_carga'}),
            #'visual_cerrado_unidad': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_cerrado_unidad'}),
            #dddddd
            'hora_inicio_carga': forms.TextInput(attrs={'class':'form-control'}),
            'hora_fin_carga': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class clientesForm(forms.ModelForm):
    class Meta:
        model =cliente
        
        fields = '__all__' 
        labels = {
            'nombre_cliente':'Nombre del cliente:',
            'direccion_fiscal':'Direccion fiscal:',
            'contacto_dir':'Contacto:',
        }

        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'direccion_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'contacto_dir': forms.TextInput(attrs={'class':'form-control'}),
        }

class TarimaForm(forms.ModelForm):
    class Meta:
        model =Tarima
        
        fields = '__all__' 
        labels = {
            'numero_tarima':'Tarima:',
            'lote_tarima':'Numero de lote:',
            'producto_tarima':'Producto:',
            'camas_tarima':'Numero de camas:',
            'paquetes_tarima':'Numero de paquetes:',
            'latas_tarima':'Lata:',
            'charolas_tarima':'Charolas:',
            'emplayado_tarima':'Emplayado:',
            'observaciones_tarima':'Observaciones:',
            #'numero_registros':'Tarimas:',
        }

        widgets = {
            
            'numero_tarima': forms.NumberInput(attrs={'class':'form-control'}),
            'lote_tarima': forms.TextInput(attrs={'class':'form-control'}),
            'producto_tarima': forms.TextInput(attrs={'class':'form-control'}),
            'camas_tarima': forms.NumberInput(attrs={'class':'form-control'}),
            'paquetes_tarima': forms.NumberInput(attrs={'class':'form-control'}),            
            'latas_tarima': forms.Select(choices=[('SI', 'SI'), ('NO', 'NO')]),
            'charolas_tarima': forms.Select(choices=[('SI', 'SI'), ('NO', 'NO')]),
            'emplayado_tarima': forms.Select(choices=[('SI', 'SI'), ('NO', 'NO')]),
            'observaciones_tarima': forms.TextInput(attrs={'class':'form-control'}),
            

        }

class contenido2Form(forms.ModelForm):
    class Meta:
        model =contenido2
        
        fields = '__all__' 
        labels = {
            'nombre_cliente':'Nombre del cliente:',
            'direccion_fiscal':'Direccion fiscal:',
            'contacto_dir':'Contacto:',
            #fffffffff
            'empresa_transportadora':'Empresa transportadora:',
            'nombre_transportista':'Nombre del transportista:',
            'licencia':'No de licencia:',
            'certificado_fumigacion':'Certificado de fumigacion:',
            #sssss
            'tracto_camion':'Tracto camion:',
            'placas_unidad':'Placas de la unidad:',
            'placas_caja':'Placas de la caja:',
            'numero_caja':'No de caja:', 

            #puntos de revision 
            'sin_hoyos':'Sin hoyos:',
            'sin_parches':'Sin parches y/o desniveles:',
            'sin_salientes':'Sin objetos salientes:',
            'sin_laminas':'Sin laminas sueltas:',

            #puertas en buen estado

            'puertas_empaques':'Empaques en buen estado:',
            'puertas_hermetico':'Cierre hermetico:',
            'puertas_salientes':'Sin objetos salientes:',
            'puertas_laminas':'Sin laminas sueltas:',

            #condiciones de higiene

            'higiene_limpios':'Limpios:',
            'higiene_olores':'Sin olores:',
            'higiene_plagas':'Sin plagas:',

            #paredes en buen estado

            'paredes_hoyos':'Sin hoyos:',
            'paredes_parches':'Sin parches y/o desniveles:',
            'paredes_salientes':'Sin objetos salientes:',
            'paredes_laminas':'Sin laminas sueltas:',

            #techos en buen estado

            'techos_hoyos':'Sin hoyos(goteras):',
            'techos_salientes':'Sin objetos salientes:',
            'techos_laminas':'Sin laminas sueltas:',

            #condiciones externas

            'externas_llantas':'LLantas unidad:',
            'externas_refaccion':'LLanta refaccion:',
            'externas_patines':'Patines de la caja:',
            'externas_luces':'Luces completas:',
            'externas_tanque':'Tanque de combustible:',
    

            #ffffffffff
            'producto':'Producto:', 
            'cantidad_charolas':'Cantidad total de charolas:',
            #fffffffffffff
            'numero_lote':'Numero de lote:',
            'cantidad_tarimas':'Cantidad total de tarimas:',
            #dddddddd 
            'visual_paredes':'(Paredes)',
            'visual_piso':'(Piso)',
            'visual_techo':'(Techo)', 
            #dddddd
            'hora_llegada':'Hora de llegada:',
            'hora_salida':'Hora de salida:', 
            #eeeeeeeeeee
            'visual_tarima1':'Primer tarima:',
            'visual_mitad_carga' :'Mitad de carga:',
            'visual_fin_carga':'Fin de carga:',
            'visual_cerrado_unidad':'Cerrado de la unidad:',
            #gggggggg
            'hora_inicio_carga':'Hora inicio de carga:',
            'hora_fin_carga':'Hora fin de carga:',                  
                    
            }      
        
        widgets = {
           
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','id':"nombre"}),           
            'direccion_fiscal': forms.TextInput(attrs={'class':'form-control','id':"direccion"}),
            'contacto_dir': forms.TextInput(attrs={'class':'form-control','id':"contacto"}),
            #ddddddd
            'empresa_transportadora': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_transportista': forms.TextInput(attrs={'class':'form-control'}),
            'licencia': forms.TextInput(attrs={'class':'form-control'}),
            'certificado_fumigacion': forms.TextInput(attrs={'class':'form-control'}),
            #fffffff
            'tracto_camion': forms.TextInput(attrs={'class':'form-control'}),
            'placas_unidad': forms.TextInput(attrs={'class':'form-control'}),
            'placas_caja': forms.TextInput(attrs={'class':'form-control'}),
            'numero_caja': forms.TextInput(attrs={'class':'form-control'}),

            #puntos de revision 
            #pisos en buen estado
            'sin_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_parches': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #puertas en buen estado

            'puertas_empaques': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_hermetico': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #condiciones de higiene

            'higiene_limpios': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'higiene_olores': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'higiene_plagas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #paredes en buen estado

            'paredes_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_parches': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

             #techos en buen estado

            'techos_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'techos_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'techos_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

             #condiciones externas

             'externas_llantas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_refaccion': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_patines': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_luces': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_tanque': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
           
            #dddddddddd
            'producto': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_charolas': forms.TextInput(attrs={'class':'form-control'}),
            #kkkkkkkkk
            'numero_lote': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_tarimas': forms.TextInput(attrs={'class':'form-control'}),
            #tttttttttttttt
            'visual_paredes': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_paredes'}),
            'visual_piso': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_piso'}),
            'visual_techo': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_techo'}),
            #dddddddddddd
            'hora_llegada': forms.TextInput(attrs={'class':'form-control'}),
            'hora_salida': forms.TextInput(attrs={'class':'form-control'}),
            #tttttttttttttt
            'visual_tarima1': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_tarima1'}),
            'visual_mitad_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_mitad_carga'}),
            'visual_fin_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_fin_carga'}),
            'visual_cerrado_unidad': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_cerrado_unidad'}),
            #dddddd
            'hora_inicio_carga': forms.TextInput(attrs={'class':'form-control'}),
            'hora_fin_carga': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class Tarima2Form(forms.ModelForm):
    class Meta:
        model =Tarima2
        
        fields = '__all__' 
        labels = {
            'numero_tarima':'Tarima:',
            'lote_tarima':'Numero de lote:',
            'producto_tarima':'Producto:',
            'camas_tarima':'Numero de camas:',
            'paquetes_tarima':'Numero de paquetes:',
            'latas_tarima':'Lata:',
            'charolas_tarima':'Charolas:',
            'emplayado_tarima':'Emplayado:',
            'observaciones_tarima':'Observaciones:',
            
        }

        widgets = {
            
            'numero_tarima': forms.NumberInput(attrs={'class':'form-control'}),
            'lote_tarima': forms.TextInput(attrs={'class':'form-control'}),
            'producto_tarima': forms.TextInput(attrs={'class':'form-control'}),
            'camas_tarima': forms.NumberInput(attrs={'class':'form-control'}),
            'paquetes_tarima': forms.NumberInput(attrs={'class':'form-control'}),            
            'latas_tarima': forms.Select(choices=[('SI', 'SI'), ('NO', 'NO')]),
            'charolas_tarima': forms.Select(choices=[('SI', 'SI'), ('NO', 'NO')]),
            'emplayado_tarima': forms.Select(choices=[('SI', 'SI'), ('NO', 'NO')]),
            'observaciones_tarima': forms.TextInput(attrs={'class':'form-control'}),
            
}
        

class contenidoeeForm(forms.ModelForm):
    class Meta:
        model =contenido
        
        
        fields = '__all__' 
        labels = {
            'nombre_cliente':'Nombre del cliente:',
            'direccion_fiscal':'Direccion fiscal:',
            'contacto_dir':'Contacto:',
            #fffffffff
            'empresa_transportadora':'Empresa transportadora:',
            'nombre_transportista':'Nombre del transportista:',
            'licencia':'No de licencia:',
            'certificado_fumigacion':'Certificado de fumigacion:',
            #sssss
            'tracto_camion':'Tracto camion:',
            'placas_unidad':'Placas de la unidad:',
            'placas_caja':'Placas de la caja:',
            'numero_caja':'No de caja:', 

            #puntos de revision 
            'sin_hoyos':'Sin hoyos:',
            'sin_parches':'Sin parches y/o desniveles:',
            'sin_salientes':'Sin objetos salientes:',
            'sin_laminas':'Sin laminas sueltas:',

            #puertas en buen estado

            'puertas_empaques':'Empaques en buen estado:',
            'puertas_hermetico':'Cierre hermetico:',
            'puertas_salientes':'Sin objetos salientes:',
            'puertas_laminas':'Sin laminas sueltas:',

            #condiciones de higiene

            'higiene_limpios':'Limpios:',
            'higiene_olores':'Sin olores:',
            'higiene_plagas':'Sin plagas:',

            #paredes en buen estado

            'paredes_hoyos':'Sin hoyos:',
            'paredes_parches':'Sin parches y/o desniveles:',
            'paredes_salientes':'Sin objetos salientes:',
            'paredes_laminas':'Sin laminas sueltas:',

            #techos en buen estado

            'techos_hoyos':'Sin hoyos(goteras):',
            'techos_salientes':'Sin objetos salientes:',
            'techos_laminas':'Sin laminas sueltas:',

            #condiciones externas

            'externas_llantas':'LLantas unidad:',
            'externas_refaccion':'LLanta refaccion:',
            'externas_patines':'Patines de la caja:',
            'externas_luces':'Luces completas:',
            'externas_tanque':'Tanque de combustible:',
    

            #ffffffffff
            'producto':'Producto:', 
            'cantidad_charolas':'Cantidad total de charolas:',
            #fffffffffffff
            'numero_lote':'Numero de lote:',
            'cantidad_tarimas':'Cantidad total de tarimas:',
            #dddddddd 
            'visual_paredes':'(Paredes)',
            'visual_piso':'(Piso)',
            'visual_techo':'(Techo)', 
            #dddddd
            'hora_llegada':'Hora de llegada:',
            'hora_salida':'Hora de salida:', 
            #eeeeeeeeeee
            'visual_tarima1':'Primer tarima:',
            'visual_mitad_carga' :'Mitad de carga:',
            'visual_fin_carga':'Fin de carga:',
            'visual_cerrado_unidad':'Cerrado de la unidad:',
            #gggggggg
            'hora_inicio_carga':'Hora inicio de carga:',
            'hora_fin_carga':'Hora fin de carga:',                  
                    
            }      
        
        widgets = {
           
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','id':"nombre"}),           
            'direccion_fiscal': forms.TextInput(attrs={'class':'form-control','id':"direccion"}),
            'contacto_dir': forms.TextInput(attrs={'class':'form-control','id':"contacto"}),
            #ddddddd
            'empresa_transportadora': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_transportista': forms.TextInput(attrs={'class':'form-control'}),
            'licencia': forms.TextInput(attrs={'class':'form-control'}),
            'certificado_fumigacion': forms.TextInput(attrs={'class':'form-control'}),
            #fffffff
            'tracto_camion': forms.TextInput(attrs={'class':'form-control'}),
            'placas_unidad': forms.TextInput(attrs={'class':'form-control'}),
            'placas_caja': forms.TextInput(attrs={'class':'form-control'}),
            'numero_caja': forms.TextInput(attrs={'class':'form-control'}),

            #puntos de revision 
            #pisos en buen estado
            'sin_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_parches': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'sin_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #puertas en buen estado

            'puertas_empaques': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_hermetico': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'puertas_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #condiciones de higiene

            'higiene_limpios': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'higiene_olores': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'higiene_plagas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

            #paredes en buen estado

            'paredes_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_parches': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'paredes_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

             #techos en buen estado

            'techos_hoyos': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'techos_salientes': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
            'techos_laminas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),

             #condiciones externas

             'externas_llantas': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_refaccion': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_patines': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_luces': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
             'externas_tanque': forms.Select(choices=[('A', 'ECEPTADO'), ('C', 'CRITICA'),('X', 'RECHAZADO'),('-', 'NO APLICA'),('N', 'NECESARIA')]),
           
            #dddddddddd
            'producto': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_charolas': forms.TextInput(attrs={'class':'form-control'}),
            #kkkkkkkkk
            'numero_lote': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_tarimas': forms.TextInput(attrs={'class':'form-control'}),
            #tttttttttttttt
            'visual_paredes': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_paredes'}),
            'visual_piso': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_piso'}),
            'visual_techo': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_techo'}),
            #dddddddddddd
            'hora_llegada': forms.TextInput(attrs={'class':'form-control'}),
            'hora_salida': forms.TextInput(attrs={'class':'form-control'}),
            #tttttttttttttt
            'visual_tarima1': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_tarima1'}),
            'visual_mitad_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_mitad_carga'}),
            'visual_fin_carga': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_fin_carga'}),
            'visual_cerrado_unidad': forms.FileInput(attrs={'class':'form-control', 'name': 'visual_cerrado_unidad'}),
            #dddddd
            'hora_inicio_carga': forms.TextInput(attrs={'class':'form-control'}),
            'hora_fin_carga': forms.TextInput(attrs={'class':'form-control'}),
            
        }

            

        









            
           





         
      

    

