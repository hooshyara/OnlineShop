from django.contrib.auth.backends import ModelBackend
from .models import User


class MobileBackend(ModelBackend):
    def authenticate(self, request, mobile, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            pass
