import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com/events") as response:
            print(response.status)
            data = await response.json()
            print(data)

asyncio.run(main())