from __future__ import unicode_literals

from django.db import models
from category.models import Category


class Article(models.Model):
    name = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(blank=False, max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category)
