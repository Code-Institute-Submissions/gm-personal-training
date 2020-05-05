# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-05 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200505_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('M', 'Mens'), ('W', 'Womens'), ('E', 'Equipment')], default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
