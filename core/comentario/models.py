# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.rh.models import Usuario
from core.post.models import Post

# Create your models here.
class Comentario(models.Model):
    class Meta:
        verbose_name = u'Comentário'
        verbose_name_plural = u'Comentários'
        app_label = "comentario"

    usuario = models.ForeignKey(Usuario)
    post = models.ForeignKey(Post, null=True, blank=True, related_name="comentario_post")
    descricao =  models.TextField()
    data_cadastro = models.DateTimeField(blank=True, verbose_name="Data Cadastro", auto_now_add=True)

    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='uploads/comentario/img/',
    )

    def __unicode__(self):
        return u"{data}".format(data =self.data_cadastro)

    def __str__(self):
        return u"{data}".format(data =self.data_cadastro)
