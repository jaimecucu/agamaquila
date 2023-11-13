from django.urls import path
from . import views



urlpatterns = [
    path('', views.menuaga, name='menuaga'),
    path('registro/',views.embarque, name='embarque'),
    path('cargas/',views.listarCarga, name='listarCarga'),
    path('editarcarga/<int:id>', views.editarCarga, name='editarCarga'),      
    path('pdf/<int:id>/', views.exportar_cargas_pdf, name='exportar_cargas_pdf'),
    path('registroClien/',views.registroCliente, name='registroCliente'),
    path('cliente/',views.listarCliente, name='listarCliente'),
    path('editarcliente/<int:id>', views.editarCliente, name='editarCliente'), 
    path('eliminarcliente/<int:id>', views.eliminarCliente, name='eliminarCliente'),     
    path("consulta_clientes/", views.consulta_clientes, name="consulta_clientes"),
    path("consulta_cliente/", views.consulta_cliente, name="consulta_cliente"),
    
]
