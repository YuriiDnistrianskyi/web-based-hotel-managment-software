from apps.booking.models.booking_to_service import BookingToService


class BookingToServiceRepository:
    _class_type = BookingToService

    def create(self, **validation_data):
        return self._class_type.factory(
            **validation_data
        )

    def get_by_booking_id(self, booking_id: int):
        return self._class_type.objects.filter(booking_id=booking_id)

    def get_by_service_id(self, service_id: int):
            return self._class_type.objects.filter(booking_id=service_id)
