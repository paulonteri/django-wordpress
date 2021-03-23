from posts.models import Tag
from posts.utils.fetch_data import fetch_tags


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
