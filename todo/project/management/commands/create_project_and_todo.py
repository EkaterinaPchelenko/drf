from django.core.management.base import BaseCommand

from todo.project.models import Project, ToDo


class Command(BaseCommand):
    def handle(self, *args, **options):
        Project.objects.create(name='project1', repository_link='https://github.com/EkaterinaPchelenko/drf')
