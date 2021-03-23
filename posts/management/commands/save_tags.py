from django.core.management.base import BaseCommand

from posts.utils.save_data import save_tags


class Command(BaseCommand):
    help = 'Save tags'

    def handle(self, *args, **kwargs):
        save_tags()
