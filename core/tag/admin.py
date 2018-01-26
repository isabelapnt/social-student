# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.tag.models import *
# Register your models here.
class TagsAdmin(admin.ModelAdmin):
    fields = ('nome', )

admin.site.register(Tags, TagsAdmin)