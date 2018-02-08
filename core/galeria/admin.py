# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.galeria.models import *
# Register your models here.
class GaleriaAdmin(admin.ModelAdmin):
    fields = ('titulo',)

class ImagensAdmin(admin.ModelAdmin):
    fields = ('imagem', 'galeria', )

admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Imagens, ImagensAdmin)
