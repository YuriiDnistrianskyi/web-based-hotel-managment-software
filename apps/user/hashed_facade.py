from django.contrib.auth.hashers import check_password, make_password


class HashedFacade:

    @staticmethod
    def hash(password: str) -> str:
        return make_password(password)

    # ?
    @staticmethod
    def verify(password: str, hashed_password: str) -> bool:
        return check_password(password, hashed_password)
