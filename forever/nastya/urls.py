from django.urls import path

from . import views

app_name = 'nastya'

urlpatterns = [
    path('', views.nastya_homepage, name='nastya_homepage')
]
