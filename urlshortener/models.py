from django.db import models

class URL(models.Model):
    source_url = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(max_length=256)

    def __str__(self):
        return self.short_url


class Image(models.Model):
    image_url = models.CharField(max_length=256)

    def __str__(self):
        return self.image_url