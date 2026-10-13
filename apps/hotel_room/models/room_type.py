from django.db import models


class RoomType(models.Model):
    """
        id int [primary key, increment]
        title varchar [not null]
    """

    title = models.CharField(max_length=50)
