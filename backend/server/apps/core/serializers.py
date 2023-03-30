from rest_framework import serializers

from core.models import ShortenedUrl


class ShortenedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = ("title", "slug", "shortened_slug", "total_visits")


class CreateShortenedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = ("slug",)
