from apps.booking.models.service import Service
from core.base_repository import BaseRepository


class ServiceRepository(BaseRepository[Service]):
    _class_type = Service
