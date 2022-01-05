from django.contrib import admin

# Register your models here.
from .models import Person, Event

admin.site.register(Person)
admin.site.register(Event)
