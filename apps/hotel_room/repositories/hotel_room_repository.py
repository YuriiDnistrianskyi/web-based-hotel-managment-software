from apps.hotel_room.models.hotel_room import HotelRoom
from core.base_repository import BaseRepository


class HotelRoomRepository(BaseRepository[HotelRoom]):
    _class_type = HotelRoom
