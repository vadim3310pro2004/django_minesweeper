from .base import *


ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://192.168.0.106:5173',
]


SIMPLE_JWT = {
    **SIMPLE_JWT,
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=30
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=30
    ),
}
