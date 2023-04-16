from django.contrib import admin
from .models import PodcastDetails,User

# Register your models here.
admin.site.register(PodcastDetails)
admin.site.register(User)