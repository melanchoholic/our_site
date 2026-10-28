from django.urls import path

from . import views

app_name = 'we'

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('films/', views.films, name='films'),
    path('gallery/', views.gallery, name='gallery'),
    path('trips/', views.TripsListView.as_view(), name='trips'),
    path('add_new_trip/', views.AddNewTripCreateView.as_view(), 
         name='add_new_trip'),
]
