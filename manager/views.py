from rest_framework import generics
from .models import Artist, Event
from .serializers import ArtistSerializer, EventSerializer


class ArtistList(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        artist = Artist.objects.all()
        return artist


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        artist = Artist.objects.all()
        return artist


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        event = Event.objects.all()
        return event


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        event = Event.objects.all()
        return event