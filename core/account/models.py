from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **kwargs):
        if username is None:
            raise TypeError ('Users must have a username!')
        if email is None:
            raise TypeError ('Users must have an email!')
        user = self.model(username = username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser (self, username, email, password):
        if password is None:
            raise TypeError ('Admins must have a password!')
        if email is None:
            raise TypeError ('Admins must have an email!')
        if username is None:
            raise TypeError ('Admins must have a username!')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
        username = models.CharField(db_index=True, max_length=255, unique=True)
        email = models.EmailField(db_index=True, unique=True, default = 'no-reply@example.com')
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        USERNAME_FIELD = 'username'
        REQUIRED_FIELDS = []
        objects = UserManager()
        def __str__(self):
            return f"{self.username} ({self.email})"