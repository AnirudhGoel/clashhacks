# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobby', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
