from .booking_repository import BookingRepository
from .booking_status_repository import BookingStatusRepository
from .booking_to_service_repository import BookingToServiceRepository
from .service_repository import ServiceRepository

booking_rep = BookingRepository()
booking_status_rep = BookingStatusRepository()
service_rep = ServiceRepository()
booking_to_service_rep = BookingToServiceRepository()
