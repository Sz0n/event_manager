from rest_framework import serializers
from .models import Artist, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event


class ArtistSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
        rel_events = validated_data.pop('events', None)
        artist = Artist.objects.create(**validated_data)
        for event in rel_events:
            event_obj = Event.objects.get(name=event["name"])
            artist.event_set.add(event_obj)
        return artist


class RelatedArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
