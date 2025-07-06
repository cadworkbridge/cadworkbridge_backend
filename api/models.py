from django.db import models
from cloudinary.models import CloudinaryField


class CardModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')  # ✅ Will save to Cloudinary
    youtube_link = models.URLField(blank=True, null=True)
    pdf_file = CloudinaryField('pdf', blank=True, null=True)
    extra_file = CloudinaryField('extra_file', blank=True, null=True)

    def __str__(self):
        return self.title
