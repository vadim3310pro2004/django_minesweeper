from faker import Faker

from rest_framework.test import APITestCase
from djoser.signals import user_activated

from .models import User


USERS_COUNT = 10


class AccountsTests(APITestCase):

    def setUp(self):
        fake = Faker("uk")

        for _ in range(USERS_COUNT):
            user = User.objects.create(
                name=fake.name(), 
                email=fake.email(), 
                password=fake.password()
            ),

            user_activated.send(sender=None, user=user[0])

    def test_users(self):
        self.assertTrue(len(User.objects.all()) == USERS_COUNT)