from core.base_state_repository import BaseStateRepository

from apps.hotel_room.models.room_type import RoomType


class RoomTypeRepository(BaseStateRepository[RoomType]):
    _class_type = RoomType
