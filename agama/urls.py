from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuaga, name='menuaga'),
]