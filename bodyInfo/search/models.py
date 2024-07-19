from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class SearchResult(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title
