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
    capasity = models.IntegerField()
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
    
