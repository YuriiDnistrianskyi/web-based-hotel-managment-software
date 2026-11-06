from services.user_service import UserService

from apps.user.repositories import user_rep

user_service = UserService(user_rep)