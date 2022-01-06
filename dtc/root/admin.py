from django.contrib import admin

# Register your models here.
from .models import Person, Event, Book

admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Book)