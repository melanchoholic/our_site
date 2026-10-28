from django import forms
from django.core.exceptions import ValidationError

from .models import Trips


class TripsForm(forms.ModelForm):

    class Meta:
        model = Trips
        fields = '__all__'
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }
