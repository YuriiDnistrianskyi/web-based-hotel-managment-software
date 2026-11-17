from django.urls import path

from apps.hotel_room.views.home_view import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]