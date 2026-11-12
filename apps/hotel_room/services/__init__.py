from apps.booking.repositories import booking_rep
from apps.hotel_room.repositories import hotel_room_rep, room_status_rep, room_type_rep

from .hotel_room_service import HotelRoomService

hotel_room_service = HotelRoomService(hotel_room_rep, room_status_rep, room_type_rep, booking_rep)
