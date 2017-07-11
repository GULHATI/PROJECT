# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-11 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msrh_user', '0020_auto_20170705_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonTrainings',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('venue', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('topic', models.CharField(blank=True, max_length=20, null=True)),
                ('head_of_program', models.CharField(blank=True, max_length=20, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='msrh_user.DEPARTMENT')),
            ],
        ),
    ]
