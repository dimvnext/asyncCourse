from time import time
from time import sleep
import asyncio


async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print("Get pages for {}".format(site_name))
    return range(1, 4)


async def get_page_data(site_name, page):
    if page == 3:
        delay = 5
    else:
        delay = 1
    await asyncio.sleep(delay)
    return "Data from page {} {}".format(page, site_name)


# def loader(url):
#     print("Load {} at {:.2f}".format(url, time() - start))


async def spider(site_name):
    pages = await get_pages(site_name)
    co_pages = []

    for page in pages:
        co_pages.append(get_page_data(site_name, page))

    for co_page in asyncio.as_completed(co_pages, timeout=3):
        try:
            data = await co_page
            print(data)
        except asyncio.TimeoutError:
            pass


start = time()

spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Forum"))
]

event_loop = asyncio.get_event_loop()
now = event_loop.time()
# event_loop.call_soon(loader, 'url1')
# event_loop.call_later(2, loader, 'url2')
# event_loop.call_at(now + 2, loader, 'url3')
event_loop.run_until_complete(asyncio.gather(*spiders))

event_loop.close()

print("{:.2f}".format(time() - start))
