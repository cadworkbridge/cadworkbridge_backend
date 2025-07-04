from django.contrib import admin
from .models import HomeCard

@admin.register(HomeCard)
class HomeCardAdmin(admin.ModelAdmin):
    list_display = ("title", "youtube_link")
    search_fields = ("title", "description")
