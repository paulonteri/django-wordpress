from django.core.management.base import BaseCommand

from common.utils import fetch_and_save_all_site_data


class Command(BaseCommand):
    help = 'Save all website data'

    def handle(self, *args, **kwargs):
        fetch_and_save_all_site_data()
