# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-29 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0015_auto_20180111_0028'),
        ('rh', '0009_auto_20180125_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidade',
            name='servico',
        ),
        migrations.AddField(
            model_name='unidade',
            name='servico',
            field=models.ManyToManyField(blank=True, related_name='servico_unidade', to='servico.Servico'),
        ),
    ]
