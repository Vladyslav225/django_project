# Register your models here.
from django.contrib import admin

from .models import Task, Contact


admin.site.register(Task)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

