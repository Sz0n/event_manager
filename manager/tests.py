import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event, Artist


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "test_username",
            "password": "test_password"
        }
        response = self.client.post("/account/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EventsViewTestCase(APITestCase):

    events_url = reverse("events_list")

    def setUp(self):
        self.event = Event.objects.create(
            name="test_event_name",
            description="test_description",
            location="test_place",
            latitude=54.5611500000000000,
            longitude=18.5312750000000000,
            date="1212-12-12")

    def test_events_list(self):
        response = self.client.get(self.events_url)
        data = response.data[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "test_event_name")


class EventCreateViewTestCase(APITestCase):

    def setUp(self):
        self.api_authentication()

    def api_authentication(self):
        user_data = {
            "username": "test_username",
            "password": "test_password"
        }
        self.client.post("/account/register/", user_data)
        token = self.client.post("/account/token/", user_data)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token.data["access"])

    def test_create_event(self):

        event_data = {
            "name": "test_event_name",
            "description": "test_description",
            "location": "test_place",
            "latitude": "54.3645330000000000",
            "longitude": "18.6173940000000000"
        }
        response = self.client.post("/events-add/", event_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ArtistsViewTestCase(APITestCase):

    artists_url = reverse("artists_list")

    def setUp(self):
        self.event = Artist.objects.create(
            name="test_artist_name",
            genre="test_genre"
        )

    def test_artist_list(self):
        response = self.client.get(self.artists_url)
        data = response.data[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "test_artist_name")
