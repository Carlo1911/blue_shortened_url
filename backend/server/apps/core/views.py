import random
import string

from django.conf import settings
from django.shortcuts import (
    redirect,
    render,
)
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import TransformerUrlForm
from .models import TransformerUrl


class ListUrlView(ListView):
    model = TransformerUrl
    template_name = "core/list.html"

    def get_queryset(self):
        return TransformerUrl.objects.all().order_by("-visited_count")[:100]


class RedirectUrlView(DetailView):
    model = TransformerUrl
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        url_object = TransformerUrl.objects.get(slug=slug)
        url_object.visited_count += 1
        url_object.save()
        return redirect(url_object.url)


class GenerateUrlView(FormView):
    form_class = TransformerUrlForm
    template_name = "core/generate.html"

    def form_valid(self, form):
        url = form.cleaned_data["url"]
        slug = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(15)
        )
        if TransformerUrl.objects.filter(slug=slug).exists():
            # Just in case the slug is already in use
            slug = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(15)
            )

        url_object = TransformerUrl.objects.create(
            url=url,
            slug=slug,
        )
        new_url = f"{settings.BASE_URL}/{url_object.slug}/"
        return render(self.request, "core/info.html", {"new_url": new_url})
