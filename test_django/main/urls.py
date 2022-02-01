from django.conf import settings
from django.urls import path, re_path

from django.urls import path

from . import views
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

if settings.DEBUG:
    schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    )


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('basket', views.basket, name='basket'),
    path('create', views.create, name='create'),
    # path('contact', ContactView.as_view(), name='contact')
    path('contact', views.contact, name='contact'),
]
