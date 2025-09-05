
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views


urlpatterns = [
    #rota, view responsavel, nome
    path('',views.home,name='home'),      
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('usuarios/excluir/<int:id>/', views.excluir, name='excluir_usuario'),
]
