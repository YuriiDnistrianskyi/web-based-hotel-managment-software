from apps.booking.repositories.booking_repository import BookingRepository
from apps.hotel_room.models.hotel_room import HotelRoom
from apps.hotel_room.repositories.hotel_room_repository import HotelRoomRepository
from apps.hotel_room.repositories.room_status_repository import RoomStatusRepository
from apps.hotel_room.repositories.room_type_repository import RoomTypeRepository
from core.base_service import BaseService


class HotelRoomService(BaseService[HotelRoom]):
    def __init__(
            self, 
            hotel_room_rep: HotelRoomRepository,
            room_status_rep: RoomStatusRepository,
            room_type_rep: RoomTypeRepository,
            booking_rep: BookingRepository,
    ):
        super().__init__(hotel_room_rep)
        self.__room_status_rep = room_status_rep
        self.__room_type_rep = room_type_rep
        self.__booking_rep = booking_rep

    def get(self, **filters):
        rooms = self._rep.get()

        if filters.get("status"):
            rooms = rooms.filter(status=self.__room_status_rep.get_by_title(filters["status"]))
        if filters.get("type"):
            rooms = rooms.filter(type=self.__room_type_rep.get_by_title(filters["type"]))
        if filters.get("capacity"):
            rooms = rooms.filter(capacity__gte=filters["capacity"])
        if filters.get("price_max"):
            rooms = rooms.filter(price__lte=filters["price_max"])

        if filters.get("check_in") and filters.get("check_out"):
            busy_rooms = self.__booking_rep.get(
                check_in__lt=filters["check_out"],
                check_out__gt=filters["check_in"]
            ).values("hotel_room_id")
            rooms = rooms.exclude(id__in=busy_rooms)

        return rooms
