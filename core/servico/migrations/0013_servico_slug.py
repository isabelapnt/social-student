# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0012_auto_20171209_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]