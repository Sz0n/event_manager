from rest_framework import serializers
from .models import Artist, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 1


class ArtistSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = Artist
        fields = ["id", "name", "genre", "events"]


class RelatedArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
