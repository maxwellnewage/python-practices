"""
asyncio & aiohttp demo
"""

import aiohttp
import asyncio
import time


async def fetch(session, url):
    start_time = time.time()

    async with session.get(url) as response:
        response_json = await response.json()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"URL: {url} | Time taken: {elapsed_time:.2f} seconds")
        return response_json


async def run():
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://jsonplaceholder.typicode.com/posts/1",
            "https://jsonplaceholder.typicode.com/posts/2",
            "https://jsonplaceholder.typicode.com/posts/3"
        ]
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    for index in range(1, 6):
        print(f"---Try #{index}---")
        asyncio.run(run())
