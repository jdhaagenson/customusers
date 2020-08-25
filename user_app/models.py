# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=30, unique=True)
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [homepage, age]

    def __str__(self):
        return self.display_name
