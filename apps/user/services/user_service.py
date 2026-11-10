from apps.user.hashed_facade import HashedFacade
from apps.user.models.user import User
from core.base_service import BaseService


class UserService(BaseService[User]):

    def create(self, **validation_data):
        email = validation_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValueError(f"User already exists with email: {email}")

        if 'password' in validation_data:
            validation_data['password'] = HashedFacade.hash(validation_data['password'])
        return super().create(**validation_data)
