from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    edad = models.IntegerField(default=0)

class Ciudad(models.Model):
    nombre=models.CharField(max_length=50)
    id_pais=models.IntegerField(default=0)

class Pais(models.Model):
    nombre = models.CharField(max_length=50)