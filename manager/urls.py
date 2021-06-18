from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>', views.ArtistDetail.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>', views.EventDetail.as_view()),
    path('rel-artists/<int:pk>', views.ArtistSameEventsList.as_view())
]
