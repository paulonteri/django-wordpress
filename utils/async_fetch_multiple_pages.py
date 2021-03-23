import asyncio

import aiohttp
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


async def async_fetch(session, url):
    async with session.get(url) as response:
        resp = await response.json()
        return resp


async def async_fetch_after_page_one(link, pages, per_page=100):
    async with aiohttp.ClientSession() as session:
        # create and run tasks
        tasks = []
        curr_page = 2
        while curr_page <= pages:
            tasks.append(
                async_fetch(
                    session,
                    f"{link}/?per_page={per_page}&page={curr_page}",
                )
            )
            curr_page += 1
        responses = await asyncio.gather(*tasks, return_exceptions=True)

        # get data
        response_data = []
        for data in responses:
            response_data += data

        return response_data


@my_timeit
def async_fetch_multiple_pages(link, per_page=100):
    # 1. fetch first page
    url = f"{link}/?per_page={per_page}"
    response = sync_fetch(url)
    # print("status: ", response.status_code)

    # 2. get number of pages and fetch their data
    pages = 1
    if 'X-WP-TotalPages' in response.headers:
        pages = int(response.headers['X-WP-TotalPages'])
    print("pages: ", pages)
    responses = asyncio.run(async_fetch_after_page_one(link, pages, per_page))
    # print(responses)
    total = response.json() + responses

    print("total count: ", len(total))
    print("DONE -----------------------------------")
    return total
