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
        date_of_birth varchar(60)
        roleId int [not null, ref: > Role.id]
        bonuses int [not null]
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=15, default=None, null=True)
    password_hash = models.CharField(max_length=400)
    date_of_birth = models.DateField(null=True, blank=True)
    role = models.ForeignKey(
        UserRoleType,
        on_delete=models.PROTECT,
        related_name="users"
    )
    bonuses = models.IntegerField(default=0)

    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @staticmethod
    def factory(**validation_data):
        role_name = validation_data.pop('role')

        validation_data['role_id'] = UserRoleType.objects.get(title=role_name).id

        return User.objects.create(
            **validation_data
        )

    def get_role(self):
        return self.role.title