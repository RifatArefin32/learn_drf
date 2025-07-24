from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User moded
class User(AbstractUser):
    # additional fields
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male')
    
    def __str__(self):
        return self.username