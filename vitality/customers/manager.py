from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email or not username:
            raise ValueError('Fields must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
