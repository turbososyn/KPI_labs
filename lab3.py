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
        print("The operation was cancelled.")
    return results
async def async_operation(data, results, has_error):
    try:
        await asyncio.sleep(1)
        if has_error:
            raise asyncio.CancelledError("The operation was cancelled.")

        results.append(data * 2)  
    except asyncio.CancelledError:
        raise 
async def cancel_operation(tasks):
    await asyncio.sleep(1.5) 
    for task in tasks:
        task.cancel()
async def main():
    arr = [1, 2, 3]
    tasks = []
    results = []
    task = asyncio.create_task(async_map(arr, async_operation))
    tasks.append(task)
    cancel_task = asyncio.create_task(cancel_operation(tasks))
    await asyncio.gather(task, cancel_task)
    print(f"Results: {results}")
asyncio.run(main())