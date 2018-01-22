# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.tag.models import Tags
# Create your models here.

class Servico(models.Model):
    class Meta:
        verbose_name = u'Serviço'
        verbose_name_plural = u'Serviços'
        app_label = "servico"

    nome = models.CharField(max_length=200, verbose_name=u"Nome do Serviço", unique=True)
    criado_por = models.CharField(max_length=200, verbose_name=u"Criado por")
    resumo = models.TextField()  
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='uploads/servico/img/',
    )
    ativo = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tags, blank=True, related_name="servico_tags")
    has_carrosel = models.BooleanField(default=False)
    has_anexo = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u"{nome}".format(nome =self.nome)

    def get_qauntidade_post(self):
        return self.post_servico.count()

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def servico_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    artigo com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade"""
    if not instance.slug:
        slug = slugify(instance.nome)
        novo_slug = slug
        contador = 0

        while Servico.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug

signals.pre_save.connect(servico_pre_save, sender=Servico)
