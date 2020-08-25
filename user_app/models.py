# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    Homepage = models.URLField(blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True)
    REQUIRED_FIELDS = [Homepage, Age]