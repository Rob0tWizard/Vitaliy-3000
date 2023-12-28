from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from customers.manager import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=50, blank=True, null=True, validators=[validate_email])
    first_name = models.CharField(max_length=50, default='first name')
    last_name = models.CharField(max_length=50, default='last name')
    username = models.CharField(unique=True, max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',
    )

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups',
    )

    def __str__(self):
        return str(self.username) if self.username else str(self.pk)