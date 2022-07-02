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
            
            alug = Alugar_quarto.objects.create(Nome=user,Tipo=quart.Tipo,Data_de_entrada=entrada,Data_de_saida=saida,Caracter=quart.Caracter,Vago=False,Preco=quart.Preco, Camas=quart.Camas, Imagem=quart.Imagem)
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