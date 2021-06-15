from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('events/', views.EventList.as_view()),

]
