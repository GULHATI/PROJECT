# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-30 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh_user', '0006_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.RemoveField(
            model_name='hod',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hod',
            name='name',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
