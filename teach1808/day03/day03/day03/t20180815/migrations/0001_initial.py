# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='语种')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='日期')),
            ],
            options={
                'verbose_name': '语言类',
                'db_table': 'languages',
            },
        ),
    ]
