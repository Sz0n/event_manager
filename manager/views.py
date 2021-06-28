from django.http import Http404
from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Event
from .serializers import ArtistSerializer, EventSerializer, RelatedArtistSerializer
from rest_framework.permissions import IsAuthenticated


class ArtistList(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        return queryset


class CreateArtist(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name",)

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


class CreateEvent(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer


class RelatedArtistsList(APIView):

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

        if request.GET.get("search") is not None:
            related_artists = related_artists.filter(name__icontains=request.GET.get("search"))

        serializer = RelatedArtistSerializer(
            related_artists.distinct().order_by(request.GET.get("ordering", "id")), many=True)

        return Response(serializer.data, status.HTTP_200_OK)
