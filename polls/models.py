from __future__ import unicode_literals
from django.db import models
from django.core import serializers
from django.http import JsonResponse

# Create your models here.
class Product(models.Model):
	key = models.CharField(max_length=255)
	value = models.CharField(max_length=255)


