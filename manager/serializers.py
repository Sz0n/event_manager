from rest_framework import serializers
from .models import Artist, Event


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            "pk",
            "name",
            "genre",
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "pk",
            "name",
            "description",
            "location",
            "latitude",
            "longitude",
            "artists",
        ]
