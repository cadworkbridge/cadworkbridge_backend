from django.db import models
from cloudinary.models import CloudinaryField

class CardModel(models.Model):
    """
    Model representing a card with a title, description, image, and optional files and a YouTube link.
    The image and files are saved to Cloudinary.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')  # Will save to Cloudinary
    youtube_link = models.URLField(blank=True, null=True)
    pdf_file = CloudinaryField('pdf', blank=True, null=True)
    extra_file = CloudinaryField('extra_file', blank=True, null=True)

    # ✅ New optional fields
    video_length = models.CharField(max_length=20, blank=True, null=True, help_text="e.g. '70 min'")
    language = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    # Optional: Define verbose names for clarity in Django admin
    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        # Optionally, you can return more information if needed
        return f"{self.title} - {self.description[:50]}"  # Show first 50 characters of description
