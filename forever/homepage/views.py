from django.shortcuts import render

from .utils import year_month_day_counter


def homepage(request):
    info = dict(zip(
            ('years', 'months', 'days', 'year_end', 'month_end', 'day_end'),
            year_month_day_counter()
            ))
    context = {'how_long': info}
    return render(request, 'homepage/first_page.html', context)
