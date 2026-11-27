from django.urls import path

from apps.dashboard.views.dashboard_view import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]
