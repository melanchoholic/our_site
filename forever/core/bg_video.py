from django.utils import timezone


def bg_video(request):
    today = timezone.localdate()
    month = today.month
    day = today.day
    if (month, day) == (10, 31):
        bg_video = 'hellowen'
    elif (month, day) == (12, 31):
        bg_video = '31_december'
    elif month == 1 and day <= 14:
        bg_video = 'new_year'
    elif month in (12, 1, 2):
        bg_video = 'winter'
    elif month in (6, 7, 8):
        bg_video = 'summer'
    elif month == 11:
        bg_video = 'harry_potter'
    else:
        bg_video = 'aurora'
    return {'bg_video': f'video/bg/{bg_video}.mp4'}
