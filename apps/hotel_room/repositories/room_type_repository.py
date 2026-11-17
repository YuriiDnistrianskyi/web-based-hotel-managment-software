from apps.hotel_room.models.room_type import RoomType
from core.base_type_repository import BaseTypeRepsoitory


class RoomTypeRepository(BaseTypeRepsoitory[RoomType]):
    _class_type = RoomType
