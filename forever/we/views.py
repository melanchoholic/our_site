from django.shortcuts import render
from django.utils import timezone

from .models import Films, AnimatedShows, Cartoons, TVShows, Photo
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


def trips(request):
    context = {}
    return render(request, 'we/trips_card.html', context)
