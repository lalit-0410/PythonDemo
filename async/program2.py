import asyncio

async def hello():
    print("Task started")
    await asyncio.sleep(2)
    print("Task complete")

asyncio.run(hello())