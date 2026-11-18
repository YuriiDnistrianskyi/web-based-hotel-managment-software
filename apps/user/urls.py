from django.urls import path

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
    path('account/', user_account_view, name='account'),
    path('account/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('user/delete/', user_delete_view, name='user_delete')
]
