from django.contrib.auth.backends import BaseBackend
from .models import Users

class BadgePinBackend(BaseBackend):
    def authenticate(self, request, badge_num=None, pin=None):
        try:
            user = Users.objects.get(badge_num=badge_num, pin=pin)
            return user
        except Users.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None