"""Views for the 'contact' app"""

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy

from . import forms


class ContactContactFormTemplateView(FormView):
    template_name = "contact/contact_form.html"
    form_class = forms.ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    
    
class ContactLocationAndApproachTemplateView(TemplateView):
    template_name = "contact/contact_location_and_approach.html"
