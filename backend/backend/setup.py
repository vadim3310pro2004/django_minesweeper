

from accounts.models import User


def setup():
    User.objects.create(
        email='test@mail.com',
        password='Aa111111',
        name='vadym',
    )