from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Character(models.Model):

    character_name = models.CharField(max_length=100)
