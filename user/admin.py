from django.contrib import admin
from user.models import CustomUser
from biorhythm.models import Event

admin.site.register(CustomUser)
admin.site.register(Event)
