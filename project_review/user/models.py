from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

import django

import datetime


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=django.utils.timezone.now)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/reviews/{self.slug}'