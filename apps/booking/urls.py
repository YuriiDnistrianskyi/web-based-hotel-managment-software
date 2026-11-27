from django.urls import path

from apps.booking.views.booking_cancel_view import cancel_booking
from apps.booking.views.booking_create_view import BookingCreateView
from apps.booking.views.booking_price_view import booking_price
from apps.booking.views.booking_update_view import BookingUpdateView
from apps.booking.views.history_view import HistoryView

urlpatterns = [
    path('bookings/', HistoryView.as_view(), name='history'),
    path('bookings/create/<int:hotel_room_id>', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/edit/<int:pk>', BookingUpdateView.as_view(), name='booking_edit'),
    path('bookings/cancel/<int:booking_id>', cancel_booking, name='booking_cancel'),
    path('bookings/price/<int:hotel_room_id>', booking_price, name='booking_price')
]
