from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Index, name='Index'),

    #cadastar e fazer login
    path('Cadastrar',views.Criar_Usuarios, name='Cadastrar'),
    path('Acesso',views.login, name ='Acesso'),
    path('Sair',views.Sair, name='Sair'),

    #Parte de alugar quarto
    path('Detalhes/<int:alug_id>',views.Deta_quarto,name='Detalhes'),
    path('Alugar/<int:alug_id>',views.Alug_quarto, name='Alugar'),

    #Ver quartos
    path('Acomodacao',views.Acom_quart, name='Acomodacao'),
    path('Camas',views.Camas, name='Camas'),
    path('Quarto',views.Tipo, name='Quarto'),
    path('Valor',views.Valor, name='Valor'),

    #Pagina do cliente
    path('Dashbord',views.Dashbord,name='Dashbord'),
    path('Editar/<int:cli_id>',views.Editar_quarto,name='Editar'),
    path('Fechar/<int:cli_id>',views.Deletar, name='Fechar'),

    #Admin
    path('Seth_admin',views.Seth, name='Seth_admin')
]