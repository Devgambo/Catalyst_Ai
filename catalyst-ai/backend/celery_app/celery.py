from celery import Celery
from app.config.settings import settings

celery = Celery(
    __name__,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=[
        # Add your task modules here
    ]
)

celery.conf.update(
    task_track_started=True,
)
