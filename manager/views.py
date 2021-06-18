from django.http import Http404
from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Event
from .serializers import ArtistSerializer, EventSerializer, RelatedArtistSerializer


class ArtistList(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        return queryset


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name",)

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


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

        if request.GET.get("search") is not None:
            related_artists = related_artists.filter(name=request.GET.get("search"))

        serializer = RelatedArtistSerializer(
            related_artists.distinct().order_by(request.GET.get("ordering", "id")), many=True)

        return Response(serializer.data, status.HTTP_200_OK)
