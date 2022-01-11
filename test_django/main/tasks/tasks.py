from celery import shared_task
from test_django.celery import app


@app.task(bind=True)
def test_celery_func(*args, **kwargs):
    print('qqqqqq')
    return None


@shared_task
def task_celery(*args, **kwargs):
    print('wwwwww')
    for item in range(10):
        print(item)

    return None