# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-15 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certmngt', '0005_rawcertificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawcertificate',
            name='raw_text',
            field=models.TextField(default='', verbose_name='Raw Text'),
            preserve_default=False,
        ),
    ]
