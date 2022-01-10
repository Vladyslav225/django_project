from django.urls import path
from .views import index, about, catalogue, basket, create, ContactView

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('catalogue', catalogue, name='catalogue'),
    path('basket', basket, name='basket'),
    path('create', create, name='create'),
    path('contact', ContactView.as_view(), name='contact')
]