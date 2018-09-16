from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import translation

import os


class HomeTemplateView(TemplateView):
    template_name = "home/home.html"
