# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 04:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0013_auto_20180203_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_unidade', to='rh.Unidade'),
        ),
    ]
