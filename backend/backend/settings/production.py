from .base import *


ALLOWED_HOSTS = [
    *os.environ["ALLOWED_HOSTS"].split(),
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

CORS_ALLOWED_ORIGINS = [
    *os.environ["FRONTEND_ORIGINS"].split(),
]

if REST_FRAMEWORK.get("DEFAULT_RENDERER_CLASSES"):
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].remove(
        "rest_framework.renderers.BrowsableAPIRenderer"
    )
else:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
        "rest_framework.renderers.JSONRenderer",
    )