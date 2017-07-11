# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-04 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msrh_user', '0018_auto_20170705_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pending_Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_count', models.IntegerField(blank=True, null=True)),
                ('dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='msrh_user.DEPARTMENT')),
                ('emp_list', models.ManyToManyField(to='msrh_user.Names')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='msrh_user.Training')),
            ],
        ),
    ]