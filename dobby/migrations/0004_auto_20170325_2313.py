# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobby', '0003_auto_20170325_2208'),
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
        migrations.RenameField(
            model_name='skill',
            old_name='skillID',
            new_name='skillId',
        ),
    ]
