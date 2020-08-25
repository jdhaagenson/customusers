# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    display_name = models.CharField(max_length=100, required=True)
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    REQUIRED_FIELDS = [homepage, age]

    def __str__(self):
        return self.display_name