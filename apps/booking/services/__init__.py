from apps.booking.repositories import booking_rep, booking_to_service_rep, service_rep

from .booking_service import BookingService
from .service_service import ServiceService

booking_service = BookingService(booking_rep, booking_to_service_rep)
service_service = ServiceService(service_rep)
# booking_to_service_rep TODO
