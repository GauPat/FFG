"""Views for the 'media' app"""

from django.views.generic.base import TemplateView


class MediaTemplateView(TemplateView):
    template_name = "media/media.html"
