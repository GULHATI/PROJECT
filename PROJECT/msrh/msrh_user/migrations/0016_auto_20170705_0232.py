# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-04 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh_user', '0015_auto_20170705_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_trainings',
            name='dept',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pending_trainings',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
