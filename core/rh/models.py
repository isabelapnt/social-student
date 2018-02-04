# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Endereco(models.Model):
    class Meta:
        abstract = True

    endereco = models.CharField(max_length=200, verbose_name=u"endereço", blank=True)
    cidade = models.CharField(max_length=80, blank=True)
    pais = models.CharField(max_length=80, verbose_name=u"país", blank=True)
    estado = models.CharField(max_length=80, blank=True)
    bairro = models.CharField(max_length=80, blank=True)
    rua = models.CharField(max_length=80, blank=True)

class Unidade(Endereco):

    class Meta:
        verbose_name = u'Unidade'
        verbose_name_plural = u'Unidades'
        app_label = "rh"

    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=25, blank=True)
    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='uploads/unidade/img/',
    )
    # thumbnail = models.ImageField(
    #     null=True,
    #     blank=True,
    #     upload_to='uploads/unidade/img/thumbnail',
    # )

    def __str__(self):
        return u'%s' % (self.nome)

    def __unicode__(self):
        return u'%s' % (self.nome)


class Usuario(User):

    class Meta:
        verbose_name = u'Usuario'
        verbose_name_plural = u'Usuarios'
        app_label = "rh"

    celular = models.CharField(max_length=20)
    unidade = models.ForeignKey(Unidade)
    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='uploads/usuario/img/',
        default='uploads/usuario/img/perfil.png'
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.set_password(self.password)

        self.username = self.email
        super(Usuario, self).save()

    def __unicode__(self):
        return u"{username}".format(username=self.username)

    def full_name(self):
        if not self.first_name:
            return self.username
        return u"{} {}".format(self.first_name, self.last_name)

class Curso(models.Model):
    class Meta:
        unique_together = ('nome', 'unidade')
        verbose_name = u'Curso'
        verbose_name_plural = u'Cursos'
        app_label = "rh"

    nome = models.TextField(max_length=50)
    unidade = models.ForeignKey(Unidade)

    def __str__(self):
        return u'%s' % (self.nome)

class Admin(Usuario):
    class Meta:
        verbose_name = u'Admin'
        verbose_name_plural = u'Admin'
        app_label = "rh"

class Aluno(Usuario):
    class Meta:
        verbose_name = u'Aluno'
        verbose_name_plural = u'Aluno'
        app_label = "rh"

    # matricula = models.TextField(max_length=20)
    idade = models.IntegerField(default=18)
    curso = models.ForeignKey(Curso, blank=True, null=True)

