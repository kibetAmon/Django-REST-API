from django.db import models


# Create your models here.

class person(models.Model):
    first_name = models.CharField(max_length=255, default=True)
    last_name = models.CharField(max_length=255)

