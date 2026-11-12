from apps.hotel_room.models.room_type import RoomType

class RoomTypeRepository:
    _class_type = RoomType

    def get_by_title(self, title: str):
        return self._class_type.objects.get(title=title)
