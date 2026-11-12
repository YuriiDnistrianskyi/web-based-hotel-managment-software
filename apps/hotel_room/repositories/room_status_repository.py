from apps.hotel_room.models.room_status_type import RoomStatusType


class RoomStatusRepository:
    _class_type = RoomStatusType

    def get_by_title(self, title: str):
        return self._class_type.objects.get(title=title)
