# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.post.models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ('titulo', 'criado_por', 'conteudo', 'servico', 'galeria')

admin.site.register(Post, PostAdmin)
