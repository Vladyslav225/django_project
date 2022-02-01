from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.views.generic import CreateView


from .forms import TaskForm, ContactForm
from .models import Task, Contact, Catalogue


def home(request):
    task = Task.objects.order_by('title') # Sorting by a certain field
    return render(request, 'main/home.html', {'task': task})


def about(request):
    return render(request, 'main/about.html')


def catalogue(request):
    prod = Catalogue.objects.order_by() # Sorting by a certain field

    return render(request, 'main/catalogue.html', {'prod': prod})


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




def contact(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Неверная регистрация'

    form = ContactForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/contact.html', context)


