from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователи'
