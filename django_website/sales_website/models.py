from django.db import models

class Inventory(models.Model):
    item = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=10)
