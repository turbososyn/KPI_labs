import asyncio
import time
from typing import Callable, List, Any
# Adebounce function that adds a delay if the task is running very quickly

async def debounce(func: Callable, delay: float, *args, **kwargs):
    start_time = time.time()
    result = await func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    #If the execution was very fast, we wait extra
    if elapsed_time < delay:
        await asyncio.sleep(delay - elapsed_time)
    return result

#Asynchronous version of map
async def async_map(func: Callable, iterable: List[Any]) -> List[Any]:
    tasks = [func(item) for item in iterable]
    return await asyncio.gather(*tasks)
#An example of an asynchronous function
async def async_square(x: int) -> int:
    await asyncio.sleep(2) 
    return x * x
