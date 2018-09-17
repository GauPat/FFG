from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import translation

import os


class MediaTemplateView(TemplateView):
    template_name = "media/media.html"
