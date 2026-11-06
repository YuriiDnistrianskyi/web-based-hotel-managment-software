from apps.user.models.user import User
from core.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    _class_type = User
