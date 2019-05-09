from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    eye_color = models.CharField(max_length=200, null=True)
    height = models.CharField(max_length=200, null=True)
    birth_year = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
