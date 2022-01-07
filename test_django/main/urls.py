from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('basket', views.basket, name='basket'),
    path('create', views.create, name='create')
]