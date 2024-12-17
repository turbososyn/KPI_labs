import asyncio
import time
from typing import Callable, List, Any
async def async_map(func: Callable, iterable: List[Any]) -> List[Any]:
    tasks = [func(item) for item in iterable]
    return await asyncio.gather(*tasks)
async def debounce(func: Callable, delay: float, *args, **kwargs):
    start_time = time.time()
    result = await func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    if elapsed_time < delay:
        await asyncio.sleep(delay - elapsed_time)
    return result
async def async_square(x: int) -> int:
    await asyncio.sleep(2)  # Імітуємо затримку
    return x * x
async def async_map_with_await(func: Callable, iterable: List[Any]) -> List[Any]:
    results = []
    for item in iterable:
        result = await func(item)
        results.append(result)
    return results