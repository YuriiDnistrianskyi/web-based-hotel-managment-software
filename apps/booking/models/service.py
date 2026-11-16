from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    @staticmethod
    def factory(**validation_data):
        return Service.objects.create(
            **validation_data
        )
