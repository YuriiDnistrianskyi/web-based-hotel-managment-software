from django.urls import path

from apps.booking.views.booking_cancel_view import cancel_booking
from apps.booking.views.booking_price_view import booking_price
from apps.booking.views.booking_update_view import BookingUpdateView
from apps.booking.views.history_view import HistoryView

urlpatterns = [
    path('history/', HistoryView.as_view(), name='history'),
    path('booking/edit/<int:pk>/', BookingUpdateView.as_view(), name='booking_edit'),
    path('booking/cancel/<int:booking_id>', cancel_booking, name='booking_cancel'),
    path('booking/price/<int:booking_id>', booking_price, name='booking_price')
]
