from django.urls import path

from core.views import ShortenedUrlView

urlpatterns = [
    path("shortened_urls/", ShortenedUrlView.as_view(), name="shortened_urls"),
]
