# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Imagens(models.Model):
    imagem = models.ImageField(upload_to='uploads/images/img/',
                              verbose_name='imagem' )

    def __unicode__(self):
        return u"{id}".format(id =self.id)
