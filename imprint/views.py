"""Views for the 'imprint' app"""

from django.views.generic.base import TemplateView


class ImprintTemplateView(TemplateView):
    template_name = "imprint/imprint.html"
