from django.urls import path

from . import views

app_name = 'gnel'

urlpatterns = [
    path('', views.gnel_homepage, name='gnel_homepage'),
    #  path('repetitor/', views.gnel_repetitor, name='gnel_repetitor')
    #  path('', views.gnel_)
    #
]
