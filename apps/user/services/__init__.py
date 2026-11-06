from apps.user.repositories import user_rep
from apps.user.services.user_service import UserService

user_service = UserService(user_rep)