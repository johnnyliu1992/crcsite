from django import template
from django.db import models
from django.forms import ModelForm
from django import forms
from crcsite.models import Question, Answer

register = template.Library()

@register.filter
def cform(value):
    """ arg """
    Q=(
	(1.7, "Yes"),
	(1, "No"),
	(1, "I don't know"),
    )
    form=forms.ChoiceField(choices=Q, widget=forms.RadioSelect())
    return form
    