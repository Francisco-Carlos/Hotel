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


#Outro banco de dados para manter o que ja esta bom
class Alugar_quarto(models.Model):
    Nome = models.ForeignKey(User, on_delete=models.CASCADE)
    Tipo = models.CharField(max_length=100)
    Data_de_entrada = models.DateField(blank=True)
    Data_de_saida = models.DateField(blank=True)
    Caracter = models.TextField(max_length=200)
    Camas = models.DecimalField(max_digits=2, decimal_places=0)
    Vago = models.BooleanField()
    Preco = models.DecimalField( max_digits=3 ,decimal_places=0)
    Imagem = models.FileField(upload_to='alug_quart/%d/%m/%Y')

   