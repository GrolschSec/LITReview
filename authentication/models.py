from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    following = models.ManyToManyField("self", related_name="followers", symmetrical=False, blank=True)
