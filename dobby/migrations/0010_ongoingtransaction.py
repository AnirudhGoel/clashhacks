# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-26 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobby', '0009_delete_ongoingtransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='OngoingTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherId', models.IntegerField()),
                ('learnerId', models.IntegerField()),
                ('skillId', models.IntegerField()),
            ],
        ),
    ]