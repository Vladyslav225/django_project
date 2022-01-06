from django.shortcuts import render
from .models import Task

# Create your views here.


def index(request):
    task = Task.objects.order_by('-id') # Sorting by a certain field
    return render(request, 'main/index.html', {'task': task, 'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html')


def pricing(request):
    return render(request, 'main/pricing.html')
