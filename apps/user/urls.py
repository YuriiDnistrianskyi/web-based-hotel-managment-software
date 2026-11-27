from django.urls import path

from apps.user.views.password_update_view import PasswordUpdateView
from apps.user.views.user_account_view import user_account_view
from apps.user.views.user_delete_view import user_delete_view
from apps.user.views.user_login_view import UserLoginView
from apps.user.views.user_logout_view import user_logout_view
from apps.user.views.user_registration_view import UserRegistrationView
from apps.user.views.user_update_view import UserUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('users/me', user_account_view, name='account'),
    path('users/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('users/edit/password', PasswordUpdateView.as_view(), name='password_edit'),
    path('users/delete/', user_delete_view, name='user_delete')
]
