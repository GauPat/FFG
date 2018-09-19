"""Forms for the 'contact' app"""

from django import forms
from django.utils.translation import gettext_lazy as _
from cProfile import label


class ContactForm(forms.Form):
    """Form to send emails."""

    name = forms.CharField(
        label=_('Name'),
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'placeholder': _('Your name'),
        })
    )
    email = forms.CharField(
        label=_('E-mail'),
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            'placeholder': _('Your email'),
        })
    )
    subject = forms.CharField(
        label=_('Subject'),
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _('The subject'),
        })
    )
    message = forms.CharField(
        label=_('Message'),
        required=True,
        max_length=1000,
        widget=forms.Textarea(attrs={
            'placeholder': _('Your message'),
        })
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print("send!")
        pass
    