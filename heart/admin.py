from django.contrib import admin
from .models import Quartos, Alugar, Alugar_quarto,Quartos_para_alugar
# Register your models here.

class List_quartos(admin.ModelAdmin):
    list_display = ('Tipo','Preco','Camas','Vago')

class List_alugar(admin.ModelAdmin):
    list_display = ('Nome','Tipo','Valor')

class List_alug_quart(admin.ModelAdmin):
    list_display = ('Nome','Tipo','Preco','Data_de_entrada','Data_de_saida')

admin.site.register(Quartos_para_alugar,List_quartos)
admin.site.register(Alugar,List_alugar)
admin.site.register(Alugar_quarto,List_alug_quart)