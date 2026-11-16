from apps.booking.models.booking_status_type import BookingStatusType
from core.base_type_repository import BaseTypeRepsoitory


class BookingStatusRepository(BaseTypeRepsoitory[BookingStatusType]):
    _class_type = BookingStatusType

    def get_by_id(self, obj_id: int) -> BookingStatusType:
        return self._class_type.objects.get(id=obj_id)
