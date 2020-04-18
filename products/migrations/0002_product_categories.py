# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-18 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('E', 'Equipment')], default=False, max_length=1),
            preserve_default=False,
        ),
    ]
