from typing import Generic, TypeVar

from django.db import models

T = TypeVar("T", bound=models.Model)

class BaseStatusRepsoitory(Generic[T]):
    _class_type: models.Model = None
    
    def get_by_title(self, title: str) -> T:
        return self._class_type.objects.get(title=title)
