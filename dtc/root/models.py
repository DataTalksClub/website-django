from django.db import models
import uuid
from django.db.models.base import Model

class Person(models.Model):
    id = models.SlugField(max_length=20, blank=False, null=False,unique=True, primary_key=True, editable=True)

    name = models.CharField(max_length=200, blank=False, null=False)
    bio = models.TextField(blank=False, null=False)
    profile_image = models.URLField(max_length=200, blank=False, null=False)
    socials = models.JSONField(blank=True, null=True)
        
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


class Book(models.Model):
    id = models.SlugField(max_length=100, blank=False, null=False,unique=True, primary_key=True, editable=True)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    authors = models.ManyToManyField('Person', blank=False)

    cover_image = models.URLField(max_length=200, blank=False, null=False)
    preview_image = models.URLField(max_length=200, blank=True, null=True)

    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)

    links = models.JSONField()

    def __str__(self):
        return self.title


class Podcast(models.Model):
    id = models.SlugField(max_length=100, blank=False, null=False, unique=True, primary_key=True, editable=True)

    title = models.CharField(max_length=200)
    guests = models.ManyToManyField('Person', blank=False)
    preview_image = models.URLField(max_length=200, blank=True, null=True)

    season = models.IntegerField(blank=False, null=False)
    episode = models.IntegerField(blank=False, null=False)

    episode_links = models.JSONField()

    links_from_guests = models.JSONField()


    transcript = models.JSONField()

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.SlugField(max_length=100, blank=False, null=False, unique=True, primary_key=True, editable=True)

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    meta_description = models.TextField(blank=False, null=False)
   
    preview_image = models.URLField(max_length=200, blank=True, null=True)
    authors = models.ManyToManyField('Person', blank=False)

    content = models.TextField(null=False, blank=False)
    draft = models.BooleanField(default=False, null=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class Tag(models.Model):
    id = models.SlugField(max_length=100, blank=False, null=False, unique=True, primary_key=True, editable=True)

    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class SpecialPost(models.Model):
    id = models.CharField(max_length=100, blank=False, null=False, unique=True, primary_key=True, editable=True)

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    meta_description = models.TextField(blank=False, null=False)
   
    preview_image = models.URLField(max_length=200, blank=True, null=True)
    
    content = models.TextField(null=False, blank=False)
   
    def __str__(self):
        return self.title

class Tool(models.Model):
    id = models.SlugField(max_length=100, blank=False, null=False,unique=True, primary_key=True, editable=True)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    speakers = models.ManyToManyField('Person', blank=False)

    icon_picture = models.URLField(max_length=200, blank=False, null=False)
    preview_image = models.URLField(max_length=200, blank=True, null=True)

    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    links = models.JSONField()

    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


    










    






