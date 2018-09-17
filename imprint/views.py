from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import translation
from django.utils.translation import gettext_lazy as _

import os


class ImprintTemplateView(TemplateView):
    template_name = "imprint/imprint.html"
    
#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx.update({
#             'street': u'Von-Hünefeld-Str. 2, 50829 Köln',
#         })
#         return ctx
