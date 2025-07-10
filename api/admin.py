from django.contrib import admin
from .models import CardModel


@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    """
    Admin interface customization for CardModel.
    Enables efficient search and display of key fields like title and youtube_link.
    """
    list_display = ("title", "youtube_link")
    search_fields = ("title", "description")
