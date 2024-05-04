from .base import *


ALLOWED_HOSTS = ['127.0.0.1']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

CORS_ALLOWED_ORIGINS = [
    *os.environ["FRONTEND_ORIGINS"].split(),
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

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": (),
}

if REST_FRAMEWORK.get("DEFAULT_RENDERER_CLASSES"):
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].remove(
        "rest_framework.renderers.BrowsableAPIRenderer"
    )
else:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
        "rest_framework.renderers.JSONRenderer",
    )