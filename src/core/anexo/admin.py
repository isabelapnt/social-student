# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.anexo.models import *
# Register your models here.
class AnexoAdmin(admin.ModelAdmin):
    fields = ('titulo', 'servico', 'tag', 'codigo', 'documento' )

admin.site.register(Anexos, AnexoAdmin)