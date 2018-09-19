"""URL Configuration for the 'home' app"""

from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from . import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
]
