from celery import shared_task
from core.models import ShortenedUrl


@shared_task
def crawl_title_from_url(shortened_url_id):
    shortened_url_object = ShortenedUrl.objects.get(id=shortened_url_id)
    # TODO: Call the function to crawl the title
    shortened_url_object.title = f"Title {shortened_url_object.id}"
    shortened_url_object.save()
