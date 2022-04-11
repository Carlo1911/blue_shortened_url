from urllib.request import urlopen

from bs4 import BeautifulSoup
from celery.utils.log import get_task_logger
from server.celery import app

from .models import TransformerUrl

logger = get_task_logger(__name__)


@app.task(bind=True, name="task.core.get_titles_from_urls")
def get_titles_from_urls(self):
    for url_object in TransformerUrl.objects.filter(title=""):

        try:
            soup = BeautifulSoup(urlopen(url_object.url))
            url_object.title = soup.title.get_text()
            url_object.save()
        except Exception as e:
            # Proble getting url or parsing it
            logger.error(e)
