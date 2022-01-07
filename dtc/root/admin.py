from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Book)
admin.site.register(Podcast)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(SpecialPost)