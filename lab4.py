import asyncio
async def async_data_generator(start, end):
    for i in range(start, end):
        await asyncio.sleep(0.1) 
        yield i 
