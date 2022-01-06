from django.core.management.base import BaseCommand

from todo.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create(first_name='kate', last_name='test', email='test222@mail.com', is_staff=True, is_active=True)