# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-05 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200505_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='slug',
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.TextField(max_length=40),
        ),
    ]
