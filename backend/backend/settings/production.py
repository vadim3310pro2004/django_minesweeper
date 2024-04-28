from .base import *


ALLOWED_HOSTS = ['127.0.0.1']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

CORS_ALLOWED_ORIGINS = [
    os.environ.get("FRONTEND_ORIGIN"),
]

SIMPLE_JWT = {
    **SIMPLE_JWT,
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=int(os.environ.get("ACCESS_TOKEN_LIFE_MINUTES"))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=int(os.environ.get("REFRESH_TOKEN_LIFE_DEYS"))
    ),
}
