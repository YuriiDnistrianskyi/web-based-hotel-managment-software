from apps.booking.repositories import booking_rep

from .booking_service import BookingService

booking_service = BookingService(booking_rep)
