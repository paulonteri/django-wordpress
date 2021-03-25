from posts.models import Tag, Category
from posts.utils.fetch_data import fetch_tags, fetch_categories


def save_tags():
    raw_data = fetch_tags()

    for data in raw_data:
        Tag.objects.update_or_create(
            id=data["id"],
            defaults={
                'slug': data["slug"],
                'name': data["name"],
                'description': data["description"],
                'taxonomy': data["taxonomy"],
                'count': data["count"],
            }
        )


def save_categories():
    raw_data = fetch_categories()

    for data in raw_data:
        Category.objects.update_or_create(
            id=data["id"],
            defaults={
                'slug': data["slug"],
                'name': data["name"],
                'description': data["description"],
                'taxonomy': data["taxonomy"],
                'count': data["count"],
                'parent': data["parent"],
            }
        )
