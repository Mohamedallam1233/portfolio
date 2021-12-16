from django.db import models
from PIL import Image
class Works(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='my_works/')
    description = models.TextField()
    link = models.URLField()
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo .path)
        output_size = (750, 500)
        img.thumbnail(output_size)
        img.save(self.photo.path)