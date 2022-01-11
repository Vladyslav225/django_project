import os
from celery import Celery
# from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django.settings')

app = Celery('test_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'test_django.main.tasks.task_celery',
        'schedule': 30.0
    },
}