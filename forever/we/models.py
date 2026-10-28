from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from core.models import BaseWatchedModel


class Films(BaseWatchedModel):

    class Meta:
        verbose_name = 'Ретинг наших фильмов'
        verbose_name_plural = 'Ретинг наших фильмов'
        ordering = ['id']


class Cartoons(BaseWatchedModel):

    class Meta:
        verbose_name = 'Ретинг наших мультов'
        verbose_name_plural = 'Ретинг наших мультов'
        ordering = ['id']


class TVShows(BaseWatchedModel):
    season_num = models.IntegerField(
        verbose_name='Сезон',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Ретинг наших сериалов'
        verbose_name_plural = 'Ретинг наших сериалов'
        ordering = ['id']


class AnimatedShows(BaseWatchedModel):
    season_num = models.IntegerField(
        verbose_name='Сезон',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Ретинг наших мультсериалов'
        verbose_name_plural = 'Ретинг наших мультсериалов'
        ordering = ['id']


class Photo(models.Model):
    image = models.ImageField(upload_to='we/gallery', verbose_name='адрес')
    description = models.CharField(verbose_name='описание', max_length=200,
                                   blank=True)
    audio = models.FileField(
        verbose_name='аудио',
        upload_to='audio/we/',
        blank=True,
        null=True,
        help_text='данное поле чисто для вайба, но вайбить много не получается'
    )
    order = models.PositiveIntegerField(
        verbose_name='доп. сортировка',
        default=0,
        help_text='данное поле лучше оставить пустым, я экспериментирую с ним'
        )
    is_published = models.BooleanField(
        default=True,
        verbose_name='опубликовано?'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.description


class Trips(models.Model):
    from_where = models.CharField(
        verbose_name='откуда',
        max_length=50,
    )
    to_where = models.CharField(
        verbose_name='куда',
        max_length=50,
    )
    travel_date = models.DateField(verbose_name='дата поездки')
    return_date = models.DateField(verbose_name='дата возвращения')
    description = models.TextField('Описание поездки')
    image1 = models.ImageField(
        verbose_name='фоточка1',
        blank=False,
        upload_to='we/trips'
    )
    image2 = models.ImageField(
            verbose_name='фоточка2',
            blank=False,
            upload_to='we/trips'
        )
    image3 = models.ImageField(
            verbose_name='фоточка3',
            blank=False,
            upload_to='we/trips'
        )
    general_vibe = models.IntegerField(verbose_name='вайб поездки')

    class Meta:
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'

    def clean(self):
        super().clean()
        errors = {}
        travel_date = self.travel_date
        return_date = self.return_date
        general_vibe = self.general_vibe

        if travel_date < settings.START:
            errors['travel_date'] = 'Мы тогда еще не могли никуда съездить :('
        if return_date < travel_date:
            tr_d_str = travel_date.strftime('%d.%m.%Y')
            errors['return_date'] = f'Дата возвращения не может быть раньше {tr_d_str}'
        if general_vibe < 0 or general_vibe > 10:
            errors['general_vibe'] = 'Оценка от 0 до 10'

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"поездка {self.from_where} - {self.to_where}"
