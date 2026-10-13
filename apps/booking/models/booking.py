from django.db import models

from apps.booking.models.booking_status_type import BookingStatusType
from apps.hotel_room.models.hotel_room import HotelRoom
from apps.user.models.user import User


class Booking(models.Model):
    """
        id int [primary key, increment]
        roomId int [not null, ref: > HotelRoom.id]
        userId int [not null, ref: > User.id]
        checkInDate date [not null]
        checkOutDate date [not null]
        meals bool [not null]
        transfer bool [not null]
        spa bool [not null]
        price int [not null]
        statusId int [not null, ref: > BookingStatusType.id]
    """

    room = models.ForeignKey(
        HotelRoom,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    checkInDate = models.DateField()
    checkOutDate = models.DateField()
    meals = models.BooleanField(default=False) # ?
    transfer = models.BooleanField(default=False) # ?
    spa = models.BooleanField(default=False) # ?
    price = models.IntegerField()

    status = models.ForeignKey(
        BookingStatusType,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
