from faker import Faker
from pprint import pprint

from django.urls import reverse
from rest_framework.test import APITestCase
from djoser.signals import user_activated

from minesweeper.models import Player
from accounts.models import User


USERS_COUNT = 10


class MinesweeperTests(APITestCase):

    def setUp(self) -> None:
        fake = Faker("uk")

        for _ in range(USERS_COUNT):
            user = (
                User.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    password=fake.password(),
                ),
            )

            user_activated.send(sender=None, user=user[0])

    def test_players(self):
        self.assertEqual(USERS_COUNT, len(Player.objects.all()))
