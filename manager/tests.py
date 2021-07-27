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


class ReceiveTokenTestCase(APITestCase):

    user_data = {
        "username": "test_username",
        "password": "test_password"
    }

    def setUp(self):
        self.client.post("/account/register/", self.user_data)

    def test_token(self):
        response = self.client.post("/account/token/", self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "access")

    def test_token_unauthenticated(self):
        not_user_data = {
            "username": "test_wrong_username",
            "password": "test_wrong_password"
        }
        response = self.client.post("/account/token/", not_user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


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

    event_data = {
        "name": "test_event_name",
        "description": "test_description",
        "location": "test_place",
        "latitude": "54.3645330000000000",
        "longitude": "18.6173940000000000"
    }

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

    def test_create_event_authenticated(self):
        response = self.client.post("/events-add/", self.event_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_event_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post("/events-add/", self.event_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


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
