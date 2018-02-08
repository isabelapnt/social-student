# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Galeria(models.Model):
    titulo = models.CharField(max_length=200, verbose_name=u"Titulo")

    def __unicode__(self):
        return u"{titulo}".format(titulo =self.titulo)

    def __str__(self):
        return u"{titulo}".format(titulo =self.titulo)

class Imagens(models.Model):
    imagem = models.ImageField(upload_to='uploads/images/img/',
                              verbose_name='imagem' )
    galeria = models.ForeignKey(Galeria, null=True, blank=True, related_name="imagem_galeria")

    def __unicode__(self):
        return u"{titulo}".format(titulo =self.galeria.titulo)

    def __str__(self):
        return u"{titulo}".format(titulo =self.galeria.titulo)
