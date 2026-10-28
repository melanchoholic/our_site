from django.db import models


class BaseWatchedModel(models.Model):
    title = models.CharField(verbose_name='название', max_length=50)
    year = models.IntegerField(verbose_name='год выхода')
    who_chose = models.CharField(verbose_name='кто выбрал', max_length=50)
    gnel_rating = models.DecimalField(verbose_name='оценка Гнэла')
    nastya_rating = models.DecimalField(verbose_name='оценка Насти')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
