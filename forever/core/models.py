from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseWatchedModel(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50,
        help_text='название',
    )
    year = models.IntegerField(
        verbose_name='год выхода',
        help_text='год выхода',
    )
    who_chose = models.CharField(
        verbose_name='кто выбрал',
        max_length=50,
        help_text='кто выбрал',
    )
    gnel_rating = models.DecimalField(
        verbose_name='оценка Гнэла',
        help_text='оценка Гнэла',
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    nastya_rating = models.DecimalField(
        verbose_name='оценка Насти',
        help_text='оценка Насти',
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
