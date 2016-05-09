from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    full_name = models.CharField(blank=False, max_length=255)
    tile = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=False, max_length=255)
    content = models.TextField()
