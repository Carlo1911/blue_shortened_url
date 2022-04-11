import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.prod")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update-title-from-urls": {
        "task": "task.core.get_titles_from_urls",
        "schedule": crontab(hour="*"),
    },
}
