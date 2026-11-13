from core.base_state_repository import BaseStateRepository

from apps.hotel_room.models.room_status_type import RoomStatusType


class RoomStatusRepository(BaseStateRepository[RoomStatusType]):
    _class_type = RoomStatusType
