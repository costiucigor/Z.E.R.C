from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    # Define the allowed role names using choices
    ROLE_CHOICES = [
        ('administrator', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    name = models.CharField(max_length=15, choices=ROLE_CHOICES)


class User(AbstractUser):
    roles = models.ManyToManyField(Role)
