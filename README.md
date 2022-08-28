# Seth Hotel 

Tecnologias usadas:
 - HTML
 - Python
 - CSS

## Processo de criação back-end
 - [x] Criação do banco de dados e seus relacionametos 
 - [x] Criação da funçoes 
 - [x] Criação das rotas de acesso
 
 ### Banco de dados:
 ```
 from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quartos(models.Model):
    Nome = models.ForeignKey(User,on_delete=models.CASCADE)
    Tipo = models.CharField(max_length=100)
    Data = models.DateField()
    Noite = models.DecimalField(max_digits=3, decimal_places=0)
    Imagem = models.FileField(upload_to=('img_quarto/%d/%m/%y'))
    Tempo_quarto = models.IntegerField()

#Vamos fazer um texto grande
class Alugar(models.Model):
    Tipo = models.CharField(max_length=100)
    Data = models.DateField(blank=True)
    Valor = models.DecimalField(max_digits=3,decimal_places=0)
    Imagem = models.FileField(upload_to='img_aluga/%d/%m/%Y')
    Noites = models.IntegerField(blank=True)
    Vago =  models.BooleanField()
    Nome = models.CharField(max_length=100,blank=True)


#Quartos para alugar
class Quartos_para_alugar(models.Model):
    Tipo = models.CharField(max_length=100)
    Data_de_entrada = models.DateField(blank=True)
    Data_de_saida = models.DateField(blank=True)
    Caracter = models.TextField(max_length=200)
    Camas = models.DecimalField(max_digits=2, decimal_places=0)
    Vago = models.BooleanField()
    Preco = models.DecimalField( max_digits=3 ,decimal_places=0)
    Imagem = models.FileField(upload_to='alug_quart/%d/%m/%Y')
 ```
### Funções a parte funcional do site:
```
from multiprocessing import context
from this import d
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Alugar_quarto, Quartos_para_alugar
# Create your views here.
def Index(request):

    alugar = Quartos_para_alugar.objects.all()
    context = {'alugar':alugar}
    return render(request,'Index.html',context)

#Crinado o usuarios, suas funçoes de login e sair
def Criar_Usuarios(request):
    if request.method == 'POST':
        nome = request.POST['Nome']
        Email = request.POST['Email']
        senha = request.POST['senha']
        senha_1 = request.POST['senha_1']

        if User.objects.filter(email=Email).exists():
            print('ja cadastrado....')
        user = User.objects.create_user(username=nome,email=Email,password=senha_1)
        user.save()
        return redirect('Index')
    else:
        return render(request,'Cadastrar.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        senha = request.POST['Senha']
        if email == '' or senha == '':
            redirect('Login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request,username=nome,password=senha)
            if user is not None:
                auth.login(request,user)
                return redirect('Index')
    return  render(request,'Acesso.html')

def Sair(request):
    auth.logout(request)
    return redirect('Index')


#Alugar Quarto, ver detalhes do guarto e alugar e encerrar
def Deta_quarto(request,alug_id):
    alug = Quartos_para_alugar.objects.get(id=alug_id)
    quart = Quartos_para_alugar.objects.all().exclude(id=alug_id)
    context = {'alug':alug, 'quart':quart}
    return render(request,'Detalhes.html',context)

def Alug_quarto(request,alug_id):
    if request.user.is_authenticated:
        if request.POST:
            id = request.user.id
            user = get_object_or_404(User,pk=id)
            quart = Quartos_para_alugar.objects.get(id=alug_id)
            alug = Alugar_quarto.objects.all()
            entrada = request.POST['Entrada']
            saida = request.POST['Saida']

            print(f'{user.username}, -> {quart.Tipo}, -> {entrada}, -> {saida}')
            quart.Vago = False
            print('---------------')
            
            #Esse alug e tudo na mesma linha
            alug = Alugar_quarto.objects.create(Nome=user,Tipo=quart.Tipo,Data_de_entrada=entrada,
            Data_de_saida=saida,Caracter=quart.Caracter,Vago=False,Preco=quart.Preco, 
            Camas=quart.Camas, Imagem=quart.Imagem)
            alug.save()
            quart.save()
            print('Deu certo')
            return redirect('Dashbord')
    else:
        return render(request,'Acesso.html')        

def Acom_quart(request):
    alug = Quartos_para_alugar.objects.all()
    context ={'alugar':alug}
    return render(request,'Acomodacoes.html',context)


def Dashbord(request):
    if request.user.is_authenticated:
        id = request.user.id
        cliente = Alugar_quarto.objects.all().filter(Nome=id)
        context = {'cliente':cliente}
        return render(request,'Dashbord.html',context)
    else:
        redirect('index')

def Editar_quarto(request,cli_id):
    if request.user.is_authenticated:
        alug = Alugar_quarto.objects.get(id=cli_id)
        context = {'alugar': alug}
        if request.POST:
            saida =  request.POST['Saida']
            alug.Data_de_saida = saida
            alug.save()
            return redirect('Dashbord')
        return render(request,'Editar_quarto.html',context)
        
def Deletar(request,cli_id):
    if request.user.is_authenticated:
        alug = Alugar_quarto.objects.get(id=cli_id)
        quart = Quartos_para_alugar.objects.get(id=cli_id)
        print(f'{alug.Vago} == {quart.Vago}')
        quart.Vago =True
        alug.delete()
        quart.save()
        return redirect('Dashbord')
    else:
        return render(request,'Acesso.html')
#Filtros
def Camas(request):
    alug = Quartos_para_alugar.objects.all().order_by('Camas')
    context = {'alugar':alug}
    return render(request,'Acomodacoes.html', context)

def Tipo(request):
    alug = Quartos_para_alugar.objects.all().order_by('Tipo')
    context = {'alugar':alug}
    return render(request,'Acomodacoes.html', context)

def Valor(request):
    alug = Quartos_para_alugar.objects.all().order_by('Preco')
    context = {'alugar':alug}
    return render(request,'Acomodacoes.html', context)

#admin
def Seth(request):
    clin = Alugar_quarto.objects.all()
    context ={'clin':clin}
    return render(request,'Lista_adm.html',context)
```

### Criação das urls
```
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
```

## Criação da parte front-end:
 - [x] Index pagina principal
 - [x] Pagina dos quartos
 - [x] Pagina dos detalhes dos quartos
 - [x] Dashbord
 
 ### Pagina Principal com o foco em ser atrativa
 ![Site Hotel -Index](https://user-images.githubusercontent.com/30003984/187050937-5f8e98ca-d045-418c-beee-ee8d7d08b8ad.png)
 
 Nessa pagina esta todas as informações do site , ao passar o mause nas imagens do quarto elas expandiram.
 O logo tipo do site foi criado por mim , usando o canvas assim dando mais originalidade para o site
 
 ### A pagina onde se encontra todos os quartos
 ![Hotel Seth - Quartos](https://user-images.githubusercontent.com/30003984/187051060-09b6b4ef-2093-4855-af89-fb9affaacb8f.png)
 
 Todos os quartos que tem no site, cada imagem quando for clicada , vai para uma tela onde esta os detalhes do quarto e se esta
 disponivel.
 
 ### Pagina do Quarto
![Hotel Seth - Quarto Detalhado ](https://user-images.githubusercontent.com/30003984/187052112-46fa4e09-f4b6-4b07-94fb-36c26ae48154.png)

Aqui e todas as informações sobre o quarto desejado , podendo ver valor, a quantidade de cama e se esta disponivel ou nao.
Rolando a pagina mais um pouco a os quartos que você poderar gostar os quartos mostrados sao os disponveis o ocupados nao sao mostrados.

### Dashbord
![Hotel Seth - Dashbord](https://user-images.githubusercontent.com/30003984/187052885-b16f744b-9f66-466c-8e8b-8dcb7b1ae5b1.png)

Essa tela e onde esta todos os quartos que o cliente alugou e a possiblidade de estender as estadia, além do encerramento da estadadia,
quando isso acontecer o quarto vai ser liberado par outra pessoa alugar e vai ser mostrado nas recomendações de quartos.







