# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.servico.models import *
# Register your models here.
class ServicoAdmin(admin.ModelAdmin):
    fields = ('ativo', 'nome', 'criado_por', 'resumo',  'slug', 'has_carrosel', 'has_anexo', 'imagem', 'tag', 'unidade')

admin.site.register(Servico, ServicoAdmin)