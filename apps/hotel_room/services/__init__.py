from apps.hotel_room.repositories import hotel_room_rep

from .services.hotel_room_service import HotelRoomService

hotel_room_service = HotelRoomService(hotel_room_rep)
