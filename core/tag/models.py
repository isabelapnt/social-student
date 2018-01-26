# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tags(models.Model):
    class Meta:
        verbose_name = u'Tags'
        verbose_name_plural = u'Tags'
        app_label = 'tag'

    nome = models.CharField(max_length=200, verbose_name=u"nome", unique= True)

    def __unicode__(self):
        return u"{nome}".format(nome =self.nome)
