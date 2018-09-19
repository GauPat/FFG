"""Views for the 'home' app"""

from django.views.generic.base import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "home/home.html"
