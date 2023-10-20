from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuaga, name='menuaga'),
    path('registro/',views.embarque, name='embarque'),
]