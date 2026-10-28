import calendar

from datetime import date

from django.utils import timezone
from django.conf import settings

MONTHS_IN_YEAR = 12


def year_month_day_counter():
    today = timezone.localdate()
    start = settings.START

    years = today.year - start.year
    months = today.month - start.month
    days = today.day - start.day

    if (today.month, today.day) < (start.month, start.day):
        years -= 1

    if months < 0:
        months += MONTHS_IN_YEAR

    if days < 0:
        prev_month = today.month - 1
        year_of_prev_month = today.year

        if prev_month == 0:
            prev_month = MONTHS_IN_YEAR
            year_of_prev_month = today.year - 1

        days_in_prev_month = calendar.monthrange(year_of_prev_month, prev_month)[1]
        days = today.day + days_in_prev_month - start.day

    year_end = 'лет'
    month_end = 'месяц'
    day_end = 'день'

    if years % 10 == 1 and years % 100 != 11:
        year_end = 'год'
    elif 2 <= years % 10 <= 4 and not (12 <= years % 100 <= 14):
        year_end = 'года'

    if months % 10 == 1 and months % 100 != 11:
        month_end = 'месяц'
    elif 2 <= months % 10 <= 4 and not (12 <= months % 100 <= 14):
        month_end = 'месяца'
    elif months != 0:
        month_end = 'месяцев'

    if days % 10 == 1 and days % 100 != 11:
        day_end = 'день'
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_end = 'дня'
    elif days != 0:
        day_end = 'дней'

    return years, months, days, year_end, month_end, day_end
