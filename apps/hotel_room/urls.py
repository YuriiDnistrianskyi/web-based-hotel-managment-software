from django.urls import path

from apps.hotel_room.views.home_view import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]