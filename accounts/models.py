from django.db import models
from django.contrib.auth.models import AbstractUser
from .usermanager import UserManager


class User(AbstractUser):
    GENDER  = (
        ('m' , 'مرد'),
        ('w' , 'زن')
    )
    username = None
    profile_picture = models.ImageField(upload_to='accounts/', null=True)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    province = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    national_id = models.CharField(null=True, max_length=10)
    post_id = models.CharField(null=True, max_length=9)
    born_dateTime = models.DateField(null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    backend = 'accounts.backend.MobileBackend'
