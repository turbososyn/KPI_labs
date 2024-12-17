import asyncio
import time
from typing import Callable, List, Any

# Parallel execution of tasks using asyncio (similar to async_map)
async def async_map(func: Callable, iterable: List[Any]) -> List[Any]:
    tasks = [func(item) for item in iterable]
    return await asyncio.gather(*tasks)

# A debounce function that adds a delay if the task is running very quickly
async def debounce(func: Callable, delay: float, *args, **kwargs):
    start_time = time.time()
    result = await func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    if elapsed_time < delay:
        await asyncio.sleep(delay - elapsed_time)
    return result

# An asynchronous function that simulates a delay and returns the square of a number
async def async_square(x: int) -> int:
    await asyncio.sleep(2)  
    return x * x

# Asynchronous version of async_map using async/await for synchronization
async def async_map_with_await(func: Callable, iterable: List[Any]) -> List[Any]:
    results = []
    for item in iterable:
        result = await func(item)
        results.append(result)
    return results

# Demonstration of parallel execution with async_map
async def demo():
    numbers = [1, 2, 3, 4, 5]
    
    # Call async_map for parallel execution
    print("Running async_map with asyncio.gather:")
    results = await async_map(async_square, numbers)
    print(f"Results after async_map: {results}")
    
    # Call async_map with async/await for synchronization
    print("\nRunning async_map with async/await:")
    results_with_await = await async_map_with_await(async_square, numbers)
    print(f"Results after async_map with await: {results_with_await}")
    
    # Call debounce to control the delay
    print("\nRunning debounce with async_map:")
    debounced_results = await debounce(async_map, 3, async_square, numbers)
    print(f"Results after debounce: {debounced_results}")

# Start the demo
asyncio.run(demo())