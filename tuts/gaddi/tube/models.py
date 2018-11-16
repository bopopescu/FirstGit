from django.db import models

# Create your models here.
class Apple(models.Model):
    name = models.CharField(max_length=255)
    amt = models.IntegerField()

class Orange(models.Model):
    name = models.CharField(max_length=255)
    amt = models.IntegerField()

class Tubelight(models.Model):
	title = models.CharField(max_length=100)
	voltage = models.DecimalField(max_digits=13, decimal_places=2)
	types = models.TextField(blank=False, null=False)
	summary = models.TextField(blank=False, null=False)
	featured = models.BooleanField(default=True)