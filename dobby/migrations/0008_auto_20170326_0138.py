# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-26 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobby', '0007_auto_20170326_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingtransaction',
            name='transId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]