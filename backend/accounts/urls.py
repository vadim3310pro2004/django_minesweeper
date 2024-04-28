from django.urls import path, include
from .views import (
    reset_password_view, 
    activate_email_view,
    google_auth_view
)


app_name = "accounts"


urlpatterns = (
    path("google_auth/", google_auth_view, name="google-jwt-auth"),
    path("email-activate/<uid>/<token>", activate_email_view, name="email-activate"),
    path("password-reset/<uid>/<token>", reset_password_view, name="password-reset"),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
)
