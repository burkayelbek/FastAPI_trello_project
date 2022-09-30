from os import environ
from celery import Celery
from src.service.job import status_task_celery

celery = Celery(__name__)
# should be redis:6379 for communicate with docker
celery.conf.broker_url = environ.get("CELERY_BROKER_URL", "redis://redis:6379")
celery.conf.result_backend = environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379")


@celery.task(name="celery_task")
def celery_task(celery_type, user_id):
    if celery_type == "status_task_celery":
        celery_result = status_task_celery(user_id=user_id)
        return celery_result
    return True
