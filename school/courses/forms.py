
from django.forms.models import inlineformset_factory
from django import forms
from .models import Course, Module


moduleFormSet = inlineformset_factory(Course, Module,
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete=True)

