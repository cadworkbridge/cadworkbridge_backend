from django.contrib import admin
from .models import CardModel

@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ("title", "youtube_link", "video_length", "language", "price")
    search_fields = ("title", "description", "language")
