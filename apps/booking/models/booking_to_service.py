from django.db import models

from .booking import Booking
from .service import Service


class BookingToService(models.Model):
    booking = models.ForeignKey(
        Booking,
        on_delete=models.PROTECT,
        related_name='booking_services'
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name='booking_services'
    )

    price = models.DecimalField(
       max_digits=10,
       decimal_places=2
    )

    @staticmethod
    def factory(**validation_data):
        return BookingToService.objects.create(
            **validation_data
        )
