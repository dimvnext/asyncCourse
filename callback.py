from time import time
from time import sleep
import asyncio
import functools


async def get_pages(site_name):
    if site_name == "API":
        await asyncio.sleep(0.1)
    else:
        await asyncio.sleep(0.5)
    await asyncio.sleep(0.5)
    print("Get pages for {}".format(site_name))
    return range(1, 4)


async def get_page_data(site_name, page, future):
    await asyncio.sleep(1)
    future.set_result("Data from page {} {}".format(page, site_name))
    return "Data from page {} {}".format(page, site_name)


def upper_data(future):
    print(future.result().upper())


def convert_data(method, future):
    result = future.result()
    print(getattr(result, method)())


def convert_data2(func, future):
    print(func(future.result))


async def spider(site_name):
    pages = await get_pages(site_name)
    for page in pages:
        future = asyncio.Future()
        future.add_done_callback(upper_data)
        future.add_done_callback(functools.partial(convert_data, 'lower'))
        future.add_done_callback(functools.partial(convert_data, 'title'))
        await get_page_data(site_name, page, future)
        # convert_data2(str.upper,data)


start = time()

spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Forum")),
    asyncio.ensure_future(spider("API"))
]

event_loop = asyncio.get_event_loop()
now = event_loop.time()
# event_loop.call_soon(loader, 'url1')
# event_loop.call_later(2, loader, 'url2')
# event_loop.call_at(now + 2, loader, 'url3')
event_loop.run_until_complete(asyncio.gather(*spiders))
event_loop.close()

print("{:.2f}".format(time() - start))
