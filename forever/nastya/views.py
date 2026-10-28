from django.shortcuts import render

from core.constants import TEXT_ABOUT_NASTYA


def nastya_homepage(request):
    context = {'text': TEXT_ABOUT_NASTYA}
    return render(request, 'nastya/nastya_homepage.html', context)
