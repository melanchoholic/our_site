from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin

from .models import Films, Cartoons, TVShows, AnimatedShows, Photo


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'year',
        'who_chose',
        'gnel_rating',
        'nastya_rating'
    )
    search_fields = ('title',)


@admin.register(Cartoons)
class CartoonsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'year',
        'who_chose',
        'gnel_rating',
        'nastya_rating'
    )
    search_fields = ('title',)


@admin.register(TVShows)
class TVShowsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'season_num',
        'year',
        'who_chose',
        'gnel_rating',
        'nastya_rating'
    )
    search_fields = ('title',)


@admin.register(AnimatedShows)
class AnimatedShowsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'season_num',
        'year',
        'who_chose',
        'gnel_rating',
        'nastya_rating'
    )
    search_fields = ('title',)


@admin.register(Photo)
class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('description', 'order', 'is_published', 'image')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('description',)
