from environs import Env

from utils.sync_fetch_multiple_pages import sync_fetch_multiple_pages

env = Env()
base_url = env('BASE_URL')


def fetch_tags():
    data = sync_fetch_multiple_pages(f"{base_url}/tags")
    return data
