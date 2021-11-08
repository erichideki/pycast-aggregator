from django.contrib import admin

from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_diplay = ("podcast_name", "title", "pub_date")
