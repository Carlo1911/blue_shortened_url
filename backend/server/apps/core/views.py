from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from core.constants import TOP_NUMBER
from core.models import ShortenedUrl
from core.serializers import (
    CreateShortenedUrlSerializer,
    ShortenedUrlSerializer,
)
from utils.algorythm import bijective_encode


class ShortenedUrlView(ListCreateAPIView):
    queryset = ShortenedUrl.objects.all().order_by("-total_visits")[:TOP_NUMBER]
    serializer_class = ShortenedUrlSerializer

    def create(self, request, *args, **kwargs):
        # Generate the shortened url
        # Check if the url already exists
        if ShortenedUrl.objects.filter(slug=request.data["slug"]).exists():
            shortened_url_object = ShortenedUrl.objects.get(slug=request.data["slug"])
            response_serializer = ShortenedUrlSerializer(shortened_url_object)
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        serializer = CreateShortenedUrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Save into database
        shortened_url_object = ShortenedUrl.objects.create(
            slug=serializer.data.get("slug")
        )
        shortened_url_object.shortened_slug = (
            f"{settings.BASE_URL}/{bijective_encode(shortened_url_object.id)}"
        )
        shortened_url_object.save()
        headers = self.get_success_headers(serializer.data)
        # Call celery task to crawl the title
        # crawl_title_from_url.delay(shortened_url_object.id)
        response_serializer = ShortenedUrlSerializer(shortened_url_object)
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
