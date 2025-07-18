from celery import Celery

celery_app = Celery(
    "docker_tasks",
    broker="redis://redis_broker:6379/0",
    backend="redis://redis_broker:6379/0"
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    result_expires=3600,
)
