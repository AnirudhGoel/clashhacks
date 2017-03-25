# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('userId', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=40)),
                ('password', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('skillID', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('skillName', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dobby.Login')),
            ],
        ),
    ]