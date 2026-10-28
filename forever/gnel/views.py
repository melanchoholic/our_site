from django.shortcuts import render

from core.constants import TEXT_ABOUT_GNEL


def gnel_homepage(request):
    context = {'text': TEXT_ABOUT_GNEL}
    return render(request, 'gnel/gnel_homepage.html', context)
