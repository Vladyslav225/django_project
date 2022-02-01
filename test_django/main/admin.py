# Register your models here.
from django.contrib import admin

from .models import Task, Contact, Item, Catalogue


admin.site.register(Task)
admin.site.register(Contact)
admin.site.register(Item)
admin.site.register(Catalogue)

