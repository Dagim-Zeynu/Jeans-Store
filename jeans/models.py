from django.db import models

# Create your models here.
class JeansStore(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.FloatField()
    image = models.CharField(max_length=3000)