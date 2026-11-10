from django.urls import path

from apps.user.views.user_login_view import UserLoginView
from apps.user.views.user_registration_view import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
