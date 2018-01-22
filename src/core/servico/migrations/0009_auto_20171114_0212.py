# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0008_auto_20171112_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='anexos',
            name='codigo',
            field=models.CharField(default=1, max_length=200, verbose_name='Codigo'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='anexos',
            unique_together=set([('tag', 'codigo')]),
        ),
    ]
