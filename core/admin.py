from django.contrib import admin
from .models import CardModel # Assuming CardModel is in your app's models.py

@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    # Customize the list view in the admin
    list_display = (
        'title',
        'youtube_link',
        'video_length',
        'language',
        'price',
        'image', # You can display the image field, though it won't render the image directly
        'pdf_file',
        'extra_file',
    )
    # Add search capability
    search_fields = ('title', 'description', 'language')

    # Add filters to the sidebar
    list_filter = ('language', 'price') # You can filter by language and price

    # Customize the form for adding/editing a CardModel instance
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'youtube_link')
        }),
        ('Additional Files', {
            'fields': ('pdf_file', 'extra_file'),
            'classes': ('collapse',), # Makes this section collapsable
        }),
        ('Card Details', {
            'fields': ('video_length', 'language', 'price'),
        }),
    )

    # Make description a textarea with a larger size (optional)
    # formfield_overrides = {
    #     models.TextField: {'widget': admin.widgets.AdminTextarea(attrs={'rows': 4, 'cols': 80})},
    # }

    # Set ordering of the list (optional)
    ordering = ('title',)

    # Prepoulated slug fields (useful if you had a slug field, not directly applicable here but good to know)
    # prepopulated_fields = {'slug': ('title',)}