# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-04 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msrh_user', '0017_auto_20170705_0253'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Names',
        ),
        migrations.RemoveField(
            model_name='pending_trainings',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='pending_trainings',
            name='emp_list',
        ),
        migrations.RemoveField(
            model_name='pending_trainings',
            name='name',
        ),
        migrations.DeleteModel(
            name='Pending_Trainings',
        ),
    ]