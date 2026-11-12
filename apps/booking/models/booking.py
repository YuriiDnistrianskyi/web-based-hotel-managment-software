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

    hotel_room = models.ForeignKey(
        HotelRoom,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    check_in = models.DateField()
    check_out = models.DateField()
    meals = models.BooleanField(default=False) # ?
    transfer = models.BooleanField(default=False) # ?
    spa = models.BooleanField(default=False) # ?
    price = models.IntegerField()

    status = models.ForeignKey(
        BookingStatusType,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    @staticmethod
    def factory(**validation_data):
        room_number = validation_data.pop('room')
        user_email = validation_data.pop('user')
        status_name = validation_data.pop('status')

        validation_data['hotel_room_id'] = HotelRoom.objects.get(number=room_number).id
        validation_data['user_id'] = User.objects.get(email=user_email).id
        validation_data['status_id'] = BookingStatusType.objects.get(name=status_name).id

        return Booking.objects.create(
            **validation_data
        )
