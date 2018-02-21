# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.rh.models import *
# Register your models here.
class UnidadeAdmin(admin.ModelAdmin):
    fields = ('nome', 'telefone')

class UsuarioAdmin(admin.ModelAdmin):
    fields = ('email', 'celular', 'unidade')

class AdminAdmin(admin.ModelAdmin):
    fields = ('email', 'celular', 'unidade')

class AlunoAdmin(admin.ModelAdmin):
    fields = ('email', 'celular', 'unidade', 'imagem')

admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Aluno, AlunoAdmin)