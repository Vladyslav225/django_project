from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import TaskForm, ContactForm
from .models import Task, Contact
from .service import send

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


class ContactView(CreateView):
    #Displaying the signature form by email

    model = Contact
    form_class = ContactForm
    succes_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)

        return super().form_valid(form)


