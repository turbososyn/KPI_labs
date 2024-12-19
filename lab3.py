import asyncio
async def async_map(arr, async_fn):
    tasks = []
    results = []
    has_error = False
    for item in arr:
        task = asyncio.create_task(async_fn(item, results, has_error))
        tasks.append(task)
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Операцію було скасовано.")
    return results