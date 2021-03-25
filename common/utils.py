from posts.utils.save_data import save_categories, save_tags


def fetch_and_save_all_site_data():
    save_categories()
    save_tags()
