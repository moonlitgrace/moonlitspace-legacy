from django.db import models
from django.contrib.auth.models import AbstractUser


# https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    ANONYM = "anonymous"
    PERSONAL = "personal"

    PROFILE_TYPE_CHOICES = {
        ANONYM: "Anonymous",
        PERSONAL: "Personal"
    }

    # Profile config
    type = models.CharField(max_length=10, choices=PROFILE_TYPE_CHOICES, default=ANONYM, verbose_name="Profile Type")
    active = models.BooleanField(default=False)
    # Basic
    name = models.CharField(max_length=100, null=True, blank=True)
    aka = models.CharField(max_length=100, verbose_name="Also Known As", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    # Social links
    github = models.URLField(null=True, blank=True)
    discord = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name or f"Profile: {self.pk}"
