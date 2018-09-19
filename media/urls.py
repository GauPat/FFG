"""URL Configuration for the 'media' app"""

from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from . import views


urlpatterns = [
    path('', views.MediaTemplateView.as_view(), name='media'),
]
