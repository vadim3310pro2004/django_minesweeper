from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager,
    PermissionsMixin,
    AbstractUser,
)


class UserManager(BaseUserManager):

    def create_user(
        self, 
        email: str, 
        name: str, 
        password: str, 
        *args, 
        **kwargs
    ):
        """
        call to create new user
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **kwargs,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, name: str, password: str, *args, **kwargs):
        """
        Used in createsuperuser
        """

        user = self.create_user(
            email=email, 
            password=password, 
            name=name, 
            is_active=True, 
            **kwargs
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("name",)

    objects = UserManager()

    username = None
    is_staff = models.BooleanField(
        verbose_name=_("is admin"),
        default=False,
    )
    name = models.CharField(
        verbose_name=_("name"), 
        max_length=255,
    )
    is_active = models.BooleanField(
        verbose_name=_("is active"),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )
    email = models.EmailField(
        verbose_name=_("email"),
        max_length=255,
        unique=True,
    )
