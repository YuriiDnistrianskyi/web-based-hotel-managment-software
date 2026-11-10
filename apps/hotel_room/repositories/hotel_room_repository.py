from typing import TypeVar

from apps.hotel_room.models.hotel_room import HotelRoom
from core.base_repository import BaseRepository

T = TypeVar("T")

class HotelRoomRepository(BaseRepository[HotelRoom]):
    _class_type = HotelRoom

    def get(self, **filters) -> list[T]:
        return self._class_type.objects.filter(**filters)
