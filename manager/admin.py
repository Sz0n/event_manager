from django.contrib import admin
from .models import Event, Artist

admin.site.register(Artist)
admin.site.register(Event)
