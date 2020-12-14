from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):

    email = models.EmailField(('Email'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    username = None

    codeChef = models.BooleanField(default=True)
    codeForces = models.BooleanField(default=True)
    hackerEarth = models.BooleanField(default=True)
    hackerRank = models.BooleanField(default=True)
    spoj = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email