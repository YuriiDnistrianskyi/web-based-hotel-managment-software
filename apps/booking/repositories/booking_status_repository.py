from apps.booking.models.booking_status_type import BookingStatusType


class BookingStatusRepository:
    _class_type = BookingStatusType

    def get_by_title(self, title: str) -> BookingStatusType:
        return self._class_type.objects.get(title=title)

    def get_by_id(self, id: int) -> BookingStatusType:
        return self._class_type.objects.get(id=id)
