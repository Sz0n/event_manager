from rest_framework import serializers
from .models import Artist, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "location",
            "latitude",
            "longitude",
            "artists",
        ]
        depth = 1


class ArtistSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = Artist
        fields = [
            "id",
            "name",
            "genre",
            "events",
        ]
