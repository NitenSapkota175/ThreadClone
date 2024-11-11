from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .CustomUserManager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField("Date of Birth")
    profile_pic = models.ImageField(upload_to="profile_pic/", null=True, blank=True)
    bio = models.TextField(blank=True, max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "dob"]

    def __str__(self):
        return self.email
