from django.db import models
from django.db import migrations

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255) 