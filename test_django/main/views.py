from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

# Create your views here.


def index(request):
    task = Task.objects.order_by('title') # Sorting by a certain field
    return render(request, 'main/index.html', {'task': task, 'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html')


def catalogue(request):
    return render(request, 'main/catalogue.html')


def basket(request):
    return render(request, 'main/basket.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Созданная форма неверная'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create.html', context)

