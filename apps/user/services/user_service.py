from apps.user.models.user import User
from core.base_service import BaseService


class UserService(BaseService[User]):

    def create(self, **validation_data):
        # захешувати
        return super().create(**validation_data)
