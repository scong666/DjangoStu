# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名字')),
                ('price', models.IntegerField(db_column='my_price', default=300, verbose_name='价格')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='生产日期')),
                ('last_update', models.DateField(auto_now=True)),
                ('is_used', models.BooleanField(default=True, verbose_name='是否再用')),
            ],
            options={
                'verbose_name': '商品类',
                'db_table': 'comm',
            },
        ),
    ]
