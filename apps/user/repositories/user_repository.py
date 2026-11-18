from apps.user.models.user import User
from core.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    _class_type = User

    def get_active_by_email(self, email):
        return self._class_type.objects.get(email=email, is_active=True)
