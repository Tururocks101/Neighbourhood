from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hood(models.Model):
    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=30, null=True)
    occupant_count = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'

class Business(models.Model):
    business_name =models.ForeignKey( on_delete=models.CASCADE)
    owner =models.ForeignKey(User, models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.business_name}'


class User(models.Model):
    name =models.CharField( max_length= 150)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'