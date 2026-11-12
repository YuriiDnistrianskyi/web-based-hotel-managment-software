from django.urls import path

from apps.booking.views.history_view import HistoryView

urlpatterns = [
    path('history/', HistoryView.as_view(), name='history')
]
