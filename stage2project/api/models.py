from django.db import models


# Create your Person model
class Person(models.Model):
    full_name = models.CharField(max_length=200)
    slack_name = models.CharField(max_length=200)
    track = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
from django.db import models

# Create your models here.
