from django.views.generic import CreateView, ListView
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy

from .models import Films, AnimatedShows, Cartoons, TVShows, Photo, Trips
from .forms import TripsForm
from core.constants import TEXT_ABOUT_US


def about_us(request):
    context = {
               'description': TEXT_ABOUT_US
    }
    return render(request, 'we/index.html', context)


def films(request):
    media = {
        'films': Films.objects.all(),
        'cartoons': Cartoons.objects.all(),
        'twshows': TVShows.objects.all(),
        'animatedshows': AnimatedShows.objects.all()
    }
    context = {'media': media}
    return render(request, 'we/films.html', context)


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
