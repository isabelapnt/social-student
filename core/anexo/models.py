# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.servico.models import Servico
from core.tag.models import Tags
# Create your models here.
class Anexos(models.Model):
    class Meta:
        # unique_together = ('tag', 'codigo')
        verbose_name = u'Anexo'
        verbose_name_plural = u'Anexos'
        app_label = "anexo"

    documento = models.FileField(upload_to='documents/')
    titulo = models.CharField(max_length=200, verbose_name=u"Titulo")
    servico = models.ForeignKey(Servico)
    # tag = models.ForeignKey(Tags)
    codigo = models.CharField(max_length=200, verbose_name=u"Código", null=True,
        blank=True,)

    def __unicode__(self):
        return u"{titulo}".format(titulo =self.titulo)