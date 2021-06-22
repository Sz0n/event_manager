from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name="artists_list"),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name="artist_detail"),
    path('events/', views.EventList.as_view(), name="events_list"),
    path('events/<int:pk>', views.EventDetail.as_view(), name="event_detail"),
    path('rel-artists/<int:pk>', views.RelatedArtistsList.as_view(), name="related_artists")
]
