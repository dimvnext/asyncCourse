from time import time
from time import sleep
import asyncio


def loader(url):
    print("Load {} at {:.2f}".format(url, time() - start))


async def spider(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)
        print(site_name, page)


start = time()

spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Forum"))
]

event_loop = asyncio.get_event_loop()
now = event_loop.time()
event_loop.call_soon(loader, 'url1')
event_loop.call_later(2, loader, 'url2')
event_loop.call_at(now + 2, loader, 'url3')
event_loop.run_until_complete(asyncio.gather(*spiders))
event_loop.close()

print("{:.2f}".format(time() - start))
