from django.contrib.auth import authenticate, login, logout


class AuthService:
    def authenticate(self, request, email, password):
        return authenticate(request, email=email, password=password)

    def login(self, request, user):
        login(request, user)

    def logout(self, request):
        logout(request)
