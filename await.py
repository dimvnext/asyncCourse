from time import time
from time import sleep
import asyncio


async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print("Get pages for {}".format(site_name))
    return range(1, 4)


async def get_page_data(site_name, page):
    await asyncio.sleep(1)
    return "Data from page {} {}".format(page, site_name)


# def loader(url):
#     print("Load {} at {:.2f}".format(url, time() - start))


async def spider(site_name):
    all_data = []
    pages = await get_pages(site_name)
    for page in pages:
        data = await get_page_data(site_name, page)
        all_data.append(data)
    return all_data


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
result = event_loop.run_until_complete(asyncio.gather(*spiders))
print(result)
event_loop.close()

print("{:.2f}".format(time() - start))
