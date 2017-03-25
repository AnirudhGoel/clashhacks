# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobby', '0002_auto_20170325_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(max_length=10)),
                ('skillID', models.IntegerField(max_length=10)),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach', models.IntegerField(max_length=10)),
                ('learn', models.IntegerField(max_length=10)),
                ('byTime', models.BooleanField()),
                ('value', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='Name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='login',
            name='userId',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skillID',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
