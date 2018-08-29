# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-18 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t06', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='icon_url',
            field=models.CharField(max_length=255, null=True, verbose_name='头像路径'),
        ),
    ]
