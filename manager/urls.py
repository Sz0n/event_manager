from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name="artists_list"),
    path('artists-add/', views.CreateArtist.as_view(), name="add_artist"),
    path('events/', views.EventList.as_view(), name="events_list"),
    path('events-add/', views.CreateEvent.as_view(), name="add_event"),
    path('rel-artists/<int:pk>', views.RelatedArtistsList.as_view(), name="related_artists")
]
