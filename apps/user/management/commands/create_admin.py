from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from apps.user.services import user_service


class Command(BaseCommand):
    help = 'Create an administrator account'

    def handle(self, *args, **kwargs):
        try:
            email = input('Email: ')
            password = input('Password: ')

            data = {
                'first_name': 'Admin',
                'last_name': 'Admin',
                'email': email,
                'password': password,
                'role': 'Admin'
            }

            user_service.create(**data)

            self.stdout.write(
                self.style.SUCCESS('Administrator created successfully')
            )
        except ValueError as ex:
            self.stdout.write(
                self.style.ERROR(f'Error: {ex}')
            )
        except ObjectDoesNotExist as ex:
            self.stdout.write(
                self.style.ERROR(f'Error: {ex}')
            )
