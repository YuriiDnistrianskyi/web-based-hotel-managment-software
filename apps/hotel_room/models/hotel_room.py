from django.db import models

from apps.hotel_room.models.room_status_type import RoomStatusType
from apps.hotel_room.models.room_type import RoomType


class HotelRoom(models.Model):
    """
        id int [primary key, increment]
        number int [not null, unique]
        capasity int [not null]
        typeId int [not null, ref: > HotelRoomType.id]
        convenience varhar [not null] //
        price int [not null]
        statusId int [not null, ref: > RoomStatusType.id]
    """

    number = models.CharField(max_length=10)
    discription = models.TextField(
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to="hotel_room/",
        null=True,
        blank=True,
    )
    capacity = models.IntegerField()
    price = models.IntegerField()
    type = models.ForeignKey(
        RoomType,
        on_delete=models.CASCADE,
        related_name="rooms"
    )
    status = models.ForeignKey(
        RoomStatusType,
        on_delete=models.CASCADE,
        related_name="rooms"
    )

    @staticmethod
    def factory(**validation_data):
        type_name = validation_data.pop('type')
        status_name = validation_data.pop('status')

        validation_data['type_id'] = RoomType.objects.get(title=type_name).id
        validation_data['status_id'] = RoomStatusType.objects.get(title=status_name).id

        return HotelRoom.objects.create(
            **validation_data
        )
