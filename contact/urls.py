"""URL Configuration for the 'contact' app"""

from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from . import views


urlpatterns = [
    path(_('contact-form/'),
         views.ContactContactFormTemplateView.as_view(), name='contact_form'),
    path(_('location-and-approach/'),
         views.ContactLocationAndApproachTemplateView.as_view(),
         name='location_and_approach'),
]
