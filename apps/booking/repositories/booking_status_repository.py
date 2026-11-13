from core.base_state_repository import BaseStateRepository

from apps.booking.models.booking_status_type import BookingStatusType


class BookingStatusRepository(BaseStateRepository[BookingStatusType]):
    _class_type = BookingStatusType

    def get_by_id(self, obj_id: int) -> BookingStatusType:
        return self._class_type.objects.get(id=obj_id)
