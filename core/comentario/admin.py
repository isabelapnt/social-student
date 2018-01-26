# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.comentario.models import *
# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    fields = ('usuario', 'data', 'descricao')

admin.site.register(Comentario, ComentarioAdmin)