# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-08 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certmngt', '0003_auto_20180308_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcertificate',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], default='3', max_length=7, verbose_name='Priority'),
        ),
    ]
