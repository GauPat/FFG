from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import translation
import os


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = "home/home.html"
    
    def dispatch(self, request, *args, **kwargs):
#         print(request.LANGUAGE_CODE)
#         request.session[translation.LANGUAGE_SESSION_KEY] = request.POST.get('language')
#         if request.session and 'language' in request.session:
#             print(str(request.session.get('language', "sessin: NOT SET")))
#         else:
#             print("sessin: NOT SET")
#         print(request.session[translation.LANGUAGE_SESSION_KEY])
#         print(str(request.COOKIES.get('language',  "cookie: NOT SET")))
#         
#         print("Header: " + request.META['HTTP_ACCEPT_LANGUAGE'])
# 
#         if 'HTTP_ACCEPT_LANGUAGE' in request.META:
#             del request.META['HTTP_ACCEPT_LANGUAGE']
            
        # translation.activate('en')
        return TemplateView.dispatch(self, request, *args, **kwargs)