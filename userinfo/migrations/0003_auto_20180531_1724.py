# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-31 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20180531_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=models.CharField(blank=True, max_length=15, unique=True, verbose_name='Contact Numer'),
        ),
    ]
