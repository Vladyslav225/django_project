from .models import Task, Contact, Item
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task

        fields = [
            'title',
            'task'
            ]

        widgets = {
            'title': TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Введите название'
                }),
            'task': Textarea(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Введите описание'
                })
            }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        
        fields = [
            'name',
            'email'
            ]

        widgets = {
            'name': TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Введите имя'
                }),
            'email': TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Введите email'
                })
            }