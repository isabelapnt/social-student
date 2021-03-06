# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0010_auto_20171114_0215'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='anexos',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='anexos',
            name='servico',
        ),
        migrations.RemoveField(
            model_name='anexos',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='post',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='post',
            name='galeria',
        ),
        migrations.RemoveField(
            model_name='post',
            name='servico',
        ),
        migrations.DeleteModel(
            name='Anexos',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Imagens',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
