from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Event
from .serializers import ArtistSerializer, EventSerializer, RelatedArtistSerializer


class ArtistList(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        artist = Artist.objects.all()
        return artist

    def create(self, request, *args, **kwargs):
        data = request.data

        new_artist = Artist.objects.create(name=data['name'], genre=data['genre'])

        new_artist.save()

        serializer = ArtistSerializer(new_artist)

        return Response(serializer.data)


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

    def create(self, request, *args, **kwargs):
        data = request.data

        new_event = Event.objects.create(name=data['name'], description=data["description"], location=data["location"],
                                         latitude=data["latitude"], longitude=data["longitude"])

        new_event.save()

        for artist in data['artists']:
            artist_obj = Artist.objects.get(name=artist['name'])
            new_event.artists.add(artist_obj)

        serializer = EventSerializer(new_event)

        return Response(serializer.data)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        event = Event.objects.all()
        return event


class ArtistSameEventsList(APIView):

    def get_object(self, pk):
        try:
            return Artist.objects.get(id=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        related_events = self.get_object(pk).events
        related_artists = Artist.objects.none()

        for event in related_events:
            related_artists |= event.artists.all()

        serializer = RelatedArtistSerializer(related_artists.distinct(), many=True)
        return Response(serializer.data)
