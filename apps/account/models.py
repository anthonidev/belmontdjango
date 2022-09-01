from django.db import models
from django.conf import settings
from .Countries import Countries
from datetime import datetime

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(default=datetime.now)
    dni = models.CharField(max_length=8, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default='')
    city = models.CharField(
        max_length=255, choices=Countries.choices, default=Countries.Lima)
    district = models.CharField(max_length=255, default='')
    zipcode = models.CharField(
        max_length=20, default='', blank=True, null=True)

    def __str__(self):
        return self.first_name
