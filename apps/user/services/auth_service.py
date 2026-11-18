from django.contrib.auth import login, logout

from apps.user.hashed_facade import HashedFacade
from apps.user.models.user import User
from apps.user.services.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def authenticate(self, request, email=None, password=None):
        try:
            user = self._user_service.get_by_email(email)

            if not user or not user.is_active or not HashedFacade.verify(password, user.password_hash):
                return None

            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = self._user_service.get_by_id(user_id)

            if user and user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None

    def login(self, request, user):
        login(request, user)

    def logout(self, request):
        logout(request)
