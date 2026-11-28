from django.urls import path

from apps.dashboard.views.dashboard_view import DashboardView
from apps.dashboard.views.rooms_view import RoomsView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('rooms/', RoomsView.as_view(), name='admin_rooms'),
]
