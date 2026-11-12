from apps.user.repositories import user_rep

from .auth_service import AuthService
from .user_service import UserService

user_service = UserService(user_rep)
auth_service = AuthService()
