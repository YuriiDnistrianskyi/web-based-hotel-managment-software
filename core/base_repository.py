from typing import Generic, TypeVar

from django.db import models

T = TypeVar("T", bound=models.Model)


class BaseRepository(Generic[T]):
    _class_type: type[T] = None

    def get(self) -> list[T]:
        return self._class_type.objects.all()

    def get_by_id(self, obj_id: int) -> T:
        return self._class_type.objects.get(self._class, id=obj_id)

    def create(self, **validation_date) -> T:
        return self._class_type.objects.create(
            **validation_date
        )

    def update(self, object: models.Model) -> T:
        object.save()
        return object

    def delete(self, obj_id: int):
        self._class_type.objects.get(id=obj_id).delete()
