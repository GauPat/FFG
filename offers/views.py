"""Views for the 'offers' app"""

from django.views.generic.base import TemplateView


class OffersTemplateView(TemplateView):
    template_name = "offers/offers.html"
    