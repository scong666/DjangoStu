# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-26 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axfday', '0011_goods_goodstypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ac123',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='GoodsTypes',
        ),
    ]
