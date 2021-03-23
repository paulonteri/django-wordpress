import requests

from utils.time_function import my_timeit


def sync_fetch(url, payload=None, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json', }
    if payload is None:
        payload = {}
    print(url)
    #

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def fetch_after_page_one(link, pages, per_page=100):
    response_data = []
    curr_page = 2
    while curr_page <= pages:
        res = sync_fetch(f"{link}/?per_page={per_page}&page={curr_page}", )
        response_data += res.json()
        curr_page += 1

    return response_data


@my_timeit
def sync_fetch_multiple_pages(link, per_page=100):
    # 1. fetch first page
    url = f"{link}/?per_page={per_page}"
    response = sync_fetch(url)
    # print("status: ", response.status_code)

    # 2. get number of pages and fetch their data
    pages = 1
    if 'X-WP-TotalPages' in response.headers:
        pages = int(response.headers['X-WP-TotalPages'])
    print("pages: ", pages)
    responses = fetch_after_page_one(link, pages, per_page)
    # print(responses)
    total = response.json() + responses

    print("total count: ", len(total))
    print("DONE -----------------------------------")
    return total
