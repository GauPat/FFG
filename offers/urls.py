"""URL Configuration for the 'offers' app"""

from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from . import views


urlpatterns = [
    path('', views.OffersTemplateView.as_view(), name='offers'),
]
