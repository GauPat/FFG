"""URL Configuration for the 'imprint' app"""

from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from . import views


urlpatterns = [
    path('', views.ImprintTemplateView.as_view(), name='imprint'),
]
