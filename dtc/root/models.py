from django.db import models
import uuid
from django.db.models.base import Model

class Person(models.Model):

    id = models.SlugField(max_length=20, blank=False, null=False,unique=True, primary_key=True, editable=True)

    name = models.CharField(max_length=200, blank=False, null=False)
    bio = models.TextField(blank=False, null=False)
    profile_image = models.URLField(max_length=200, blank=False, null=False)
    socials = models.JSONField()
        
    def __str__(self):
        return str(self.id)

