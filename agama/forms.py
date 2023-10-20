from django import forms
from .models import contenido

class contenidoForm(forms.ModelForm):
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
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'direccion_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'contacto_dir': forms.TextInput(attrs={'class':'form-control'}),
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





         
      

    

