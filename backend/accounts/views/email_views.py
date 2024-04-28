from django.http.request import HttpRequest

from django.shortcuts import render
from django.urls import reverse_lazy


def reset_password_view(request: HttpRequest, uid: str, token: str):
    context = {
        "uid": uid,
        "token": token,
        "send_to": reverse_lazy("accounts:user-reset-password-confirm"),
    }

    return render(request, "accounts/reset_password.html", context=context)


def activate_email_view(request: HttpRequest, uid: str, token: str):
    context = {
        "uid": uid,
        "token": token,
        "send_to": request.build_absolute_uri(
            reverse_lazy("accounts:user-activation")
        ),
        "operation": request.path.split("/")[-3],
    }

    return render(request, "accounts/activate_mail.html", context=context)
