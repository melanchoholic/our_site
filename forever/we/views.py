from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse_lazy

from .models import Films, AnimatedShows, Cartoons, TVShows, Photo, Trips
from .forms import (TripsForm, FilmsForm,
                    AnimatedShowsForm, CartoonsForm, TVShowsForm,)
from core.constants import TEXT_ABOUT_US


def about_us(request):
    context = {
               'description': TEXT_ABOUT_US
    }
    return render(request, 'we/index.html', context)


def films(request):
    form_classes = {
        'film':         FilmsForm,
        'cartoon':      CartoonsForm,
        'tvshow':       TVShowsForm,
        'animatedshow': AnimatedShowsForm,
    }

    forms = {key: cls() for key, cls in form_classes.items()}

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type in form_classes:
            form = form_classes[form_type](request.POST)
            if form.is_valid():
                form.save()
                return redirect('we:films')
            forms[form_type] = form

    media = {
        'films':         Films.objects.all(),
        'cartoons':      Cartoons.objects.all(),
        'twshows':       TVShows.objects.all(),
        'animatedshows': AnimatedShows.objects.all(),
    }
    return render(request, 'we/films.html', {
        'media': media,
        'forms': forms,
    })


def gallery(request):
    photos = Photo.objects.filter(is_published=True)
    context = {'photos': photos}
    return render(request, 'we/gallery.html', context)


class TripsListView(ListView):
    model = Trips
    template_name = 'we/trips_card.html'
    context_object_name = 'trips'


class AddNewTripCreateView(CreateView):
    model = Trips
    form_class = TripsForm
    template_name = 'we/add_new_trip.html'
    success_url = reverse_lazy('we:trips')
