from apps.hotel_room.models.hotel_room import HotelRoom
from core.base_service import BaseService


class HotelRoomService(BaseService[HotelRoom]):
    def get(self, **filters):
        return self._rep.get(**filters)
