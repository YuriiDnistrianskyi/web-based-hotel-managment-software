from apps.hotel_room.models.room_status_type import RoomStatusType
from core.base_type_repository import BaseTypeRepsoitory


class RoomStatusRepository(BaseTypeRepsoitory[RoomStatusType]):
    _class_type = RoomStatusType
