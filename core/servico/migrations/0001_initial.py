# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='uploads/images/img/', verbose_name='imagem')),
            ],
        ),
    ]
