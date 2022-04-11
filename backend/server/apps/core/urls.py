from django.urls import path

from .views import (
    GenerateUrlView,
    ListUrlView,
    RedirectUrlView,
)

urlpatterns = [
    path("", ListUrlView.as_view(), name="list_url"),
    path("generate/", GenerateUrlView.as_view(), name="generate_url"),
    path("<slug:slug>/", RedirectUrlView.as_view(), name="redirect_url"),
]
