from typing import Generic, TypeVar

from django.db import models

T = TypeVar("T", bound=models.Model)


class BaseRepository(Generic[T]):
    _class_type: type[T] = None

    def get(self, **filters) -> list[T]:
        return self._class_type.objects.filter(**filters)
    
    def get_by_id(self, obj_id: int) -> T:
        return self._class_type.objects.get(id=obj_id)

    def create(self, **validation_data) -> T:
        return self._class_type.factory(
            **validation_data
        )

    def update(self, obj: models.Model) -> T:
        obj.save()
        return obj

    def delete(self, obj_id: int):
        self._class_type.objects.get(id=obj_id).delete()
