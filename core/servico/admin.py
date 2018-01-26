# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.servico.models import *
# Register your models here.
class ServicoAdmin(admin.ModelAdmin):
    fields = ('ativo', 'nome', 'criado_por', 'resumo',  'slug', 'imagem', 'tag')

admin.site.register(Servico, ServicoAdmin)