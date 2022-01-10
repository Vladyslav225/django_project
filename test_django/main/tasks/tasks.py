from celery import shared_task
from test_django.celery import app


@app.task(bind=True)
def test_celery_func(*args, **kwargs):
    print('qqqqqq')
    return