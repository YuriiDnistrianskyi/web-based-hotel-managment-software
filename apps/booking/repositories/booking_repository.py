from apps.booking.models.booking import Booking
from core.base_repository import BaseRepository


class BookingRepository(BaseRepository[Booking]):
    _class_type = Booking
