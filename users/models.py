from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    playerID = models.AutoField(primary_key=True, default=0)
    emailAddress = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    position = models.CharField(max_length=50)
    hometown = models.CharField(
        max_length=50, null=True, blank=True)
    skillLevel = models.CharField(
        max_length=50, null=True, blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    ageGroup = models.CharField(
        max_length=50, null=True, blank=True)
    playType = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'emailAddress'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    objects = UserManager()

    def __str__(self):
        return self.emailAddress
