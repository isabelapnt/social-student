# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rh', '0003_auto_20171031_1647'),
        ('comentario', '0001_initial'),
        ('servico', '0011_auto_20171128_0040'),
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('conteudo', models.TextField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data Cadastro')),
                ('comentario', models.ManyToManyField(blank=True, to='comentario.Comentario')),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.Usuario')),
                ('galeria', models.ManyToManyField(blank=True, to='galeria.Imagens')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servico.Servico')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
