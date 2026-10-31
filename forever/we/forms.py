from django import forms
from django.core.exceptions import ValidationError

from .models import Trips, Films, Cartoons, TVShows, AnimatedShows


class TripsForm(forms.ModelForm):

    class Meta:
        model = Trips
        fields = '__all__'
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }


class FilmsForm(forms.ModelForm):

    class Meta:
        model = Films
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        if Films.objects.filter(title=title).exists():
            index = Films.objects.get(title=title).pk
            raise ValidationError(
                f"Фильм '{title}' уже есть в таблице, его id - {index}"
            )
        return cleaned_data


class CartoonsForm(forms.ModelForm):

    class Meta:
        model = Cartoons
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        if Films.objects.filter(title=title).exists():
            index = Films.objects.get(title=title).pk
            raise ValidationError(
                f"Мультик '{title}' уже есть в таблице, его id - {index}"
            )
        return cleaned_data


class TVShowsForm(forms.ModelForm):

    class Meta:
        model = TVShows
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        if Films.objects.filter(title=title).exists():
            index = Films.objects.get(title=title).pk
            raise ValidationError(
                f"Мультик '{title}' уже есть в таблице, его id - {index}"
            )
        return cleaned_data


class AnimatedShowsForm(forms.ModelForm):
    class Meta:
        model = AnimatedShows
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        if Films.objects.filter(title=title).exists():
            index = Films.objects.get(title=title).pk
            raise ValidationError(
                f"Мультик '{title}' уже есть в таблице, его id - {index}"
            )
        return cleaned_data
