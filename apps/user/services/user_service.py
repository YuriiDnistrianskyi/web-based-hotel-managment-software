from apps.user.hashed_facade import HashedFacade
from apps.user.models.user import User
from core.base_service import BaseService


class UserService(BaseService[User]):
    def get_by_email(self, email: str) -> User:
        return self._rep.get_active_by_email(email)

    def create(self, **validation_data):
        email = validation_data.get('email')

        if self._rep.get(email=email, is_active=True).exists():
            raise ValueError(f"User already exists with email: {email}")

        if 'password' in validation_data:
            validation_data['password_hash'] = HashedFacade.hash(validation_data.pop('password'))
        return super().create(**validation_data)

    def delete(self, obj_id):
        obj = self._rep.get_by_id(obj_id)
        obj.is_active = False
        self._rep.update(obj)
