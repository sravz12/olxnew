from django.db import models

# Create your models here.
class Vehicles(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    company=models.CharField(max_length=100)
    fuel=models.CharField(max_length=100)
