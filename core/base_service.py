from typing import Generic, TypeVar

from django.db import models

from core.base_repository import BaseRepository

T = TypeVar("T", bound=models.Model)

class BaseService(Generic[T]):
    def __init__(self, rep: BaseRepository):
        self._rep = rep

    def get(self, **filters):
        return self._rep.get(**filters)

    def get_by_id(self, obj_id: int) -> T:
        return self._rep.get_by_id(obj_id)

    def create(self, **validation_data) -> T:
        return self._rep.create(**validation_data)

    def update(self, obj_id: int, **validation_data) -> T:
        obj = self._rep.get_by_id(obj_id)
        for field, value in validation_data.items():
            setattr(obj, field, value)

        return self._rep.update(obj)

    def delete(self, obj_id: int):
        self._rep.delete(obj_id)
    