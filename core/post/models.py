# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from core.rh.models import Usuario
from core.galeria.models import Galeria
from core.servico.models import Servico
from django.db import models
from core.tag.models import Tags

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
        app_label = "post"

    titulo = models.CharField(max_length=200, verbose_name=u"Titulo")
    criado_por = models.ForeignKey(Usuario, related_name="post_usuario")
    conteudo = models.TextField()
    data_cadastro = models.DateTimeField(blank=True, null=True, verbose_name="Data Cadastro", auto_now_add=True)
    galeria = models.ForeignKey(Galeria,  blank=True, null=True)
    servico = models.ForeignKey(Servico, related_name="post_servico")
    tag = models.ManyToManyField(Tags, blank=True, related_name="post_tags")

    def __unicode__(self):
        return u"{titulo}".format(titulo =self.titulo)