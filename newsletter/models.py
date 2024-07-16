from django.db import models

from .utils import generate_entry_id


# Create your models here.
class NewsLetterEntry(models.Model):
    entry_id = models.CharField(unique=True, max_length=255, default=generate_entry_id)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email
