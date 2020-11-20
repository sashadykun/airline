from django.db import models

# Create your models here.

# After models are created, we create migration by executing:
#  python manage.py makemigrations
#  and to apply migration - python manage.py migrate

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()