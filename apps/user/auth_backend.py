from apps.user.hashed_facade import HashedFacade
from apps.user.models.user import User


class CustomAuthBackend:
    def authenticate(self, request, email=None, password=None, **kwargs):
        if not email or not password:
            return None

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if not HashedFacade.verify(password, user.password_hash):
            return None

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
