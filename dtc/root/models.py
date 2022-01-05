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

class Event(models.Model):
    EVENT_TYPE = (
        ('podcast', 'podcast'),
        ('webinar', 'webinar'),
        ('workshop', 'workshop'),
        ('conf', 'conference')
    )
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    time = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=8, choices=EVENT_TYPE)
    event_link = models.URLField(max_length=200, blank=False, null=False)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    speakers = models.ManyToManyField('Person', blank=False)

    def __str__(self):
        return self.title






