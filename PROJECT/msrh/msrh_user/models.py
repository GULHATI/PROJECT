from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class DEPARTMENT(models.Model):
    name = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.name


class HOD(models.Model):
    Eid = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=1000, primary_key=True)
    department = models.ForeignKey(DEPARTMENT,blank=True, null=True)
    position = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.Eid


class HR(models.Model):
    Eid = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=1000)
    department = models.ForeignKey(DEPARTMENT,blank=True, null=True)
    position = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.Eid


class SUPERVISOR(models.Model):
    Eid = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=1000)
    department = models.ForeignKey(DEPARTMENT,blank=True, null=True)
    position = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.Eid


class Training(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    department = models.ForeignKey(DEPARTMENT, blank=True, null=True)
    venue = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    topic = models.CharField(max_length=20,blank=True, null=True)
    head_of_program = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name


class EMPLOYEE(models.Model):
    Eid = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=1000, primary_key=True)
    department = models.ForeignKey(DEPARTMENT,blank=True, null=True)
    trainings = models.ManyToManyField(Training)

    def __str__(self):
        return self.Eid

class Names(models.Model):
    name = models.CharField(max_length=100 , primary_key=True)
    def __str__(self):
        return self.name

class Pending_Trainings(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    dept = models.CharField(max_length=10,blank=True,null=True)
    emp_count = models.IntegerField(blank=True,null=True)
    emp_list = models.ManyToManyField(Names)

    def __str__(self):
        return self.name