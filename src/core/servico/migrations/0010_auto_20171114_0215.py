# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0009_auto_20171114_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexos',
            name='codigo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='C\xf3digo'),
        ),
    ]
