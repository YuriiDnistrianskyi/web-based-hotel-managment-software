from django.db import models

from apps.user.models.user_role_type import UserRoleType


class User(models.Model):
    """
        id int [primary key, increment]
        firstName varchar(60) [not null]
        lastName varchar(60) [not null]
        email varcahr(60) [not null, unique]
        phone varchar(60) [not null]
        passwordHash varchar(200) [not null]
        dateOdBirth varchar(60)
        roleId int [not null, ref: > Role.id]
        bonuses int [not null]
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    password_hash = models.CharField(max_length=400)
    dateOfBirth = models.DateField(auto_now_add=True)
    role = models.ForeignKey(
        UserRoleType,
        on_delete=models.CASCADE,
        related_name="users"
    )
    bonuses = models.IntegerField()

    @staticmethod
    def factory(**validation_date):
        return User.objects.create(
            **validation_date
        )