from django.urls import path
from . import views


urlpatterns = [
    path('', views.menuaga, name='menuaga'),
    path('registro/',views.embarque, name='embarque'),
    path('cargas/',views.listarCarga, name='listarCarga'),
    path('editarcarga/<int:id>', views.editarCarga, name='editarCarga'),      
    path('pdf/<int:id>/', views.exportar_cargas_pdf, name='exportar_cargas_pdf'),
    
]
