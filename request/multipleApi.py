import aiohttp
import asyncio

async def getData(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls=[
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/todos"
    ]
    async with aiohttp.ClientSession() as session:

        tasks=[getData(session,url) for url in urls ] # list comprehension

        results= await asyncio.gather(*tasks)
        
        for result in results:
            print(result)

asyncio.run(main())