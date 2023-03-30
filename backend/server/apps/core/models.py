from django.db import models


class ShortenedUrl(models.Model):
    slug = models.CharField("Original URL", max_length=100, unique=True)
    shortened_slug = models.CharField("Shortened URL", max_length=100, unique=True)
    title = models.CharField("Title", max_length=100, blank=True)
    total_visits = models.IntegerField("Total visits", default=0)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        if self.title:
            return self.title
        return self.shortened_slug

    class Meta:
        verbose_name = "Shortened URL"
        verbose_name_plural = "Shortened URLs"
