from django.core.management.base import BaseCommand

from posts.utils.save_data import save_categories


class Command(BaseCommand):
    help = 'Save categories'

    def handle(self, *args, **kwargs):
        save_categories()
