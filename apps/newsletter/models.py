from django.db import models
import uuid

# Create your models here.
class NewsLetterEntry(models.Model):
    entry_id = models.CharField(unique=True, max_length=255, default=lambda: uuid.uuid4().int)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email
