import asyncio

# AsyncMap function with cancellation support
async def async_map(arr, async_fn):
    tasks = []
    results = []
    has_error = False
    
    # Create a list of asynchronous tasks
    for item in arr:
        task = asyncio.create_task(async_fn(item, results, has_error))
        tasks.append(task)
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("The operation was cancelled.")
    return results

# Example of an asynchronous operation that can be cancelled
async def async_operation(data, results, has_error):
    try:
        
        # Simulate a delay
        await asyncio.sleep(1)
        
        # If cancelled, exit
        if has_error:
            raise asyncio.CancelledError("The operation was cancelled.")

        results.append(data * 2)  # Multiply data by 2 as an example task
    except asyncio.CancelledError:
        raise # Catch and re-raise the cancellation

# Function to cancel the operation
async def cancel_operation(tasks):
    await asyncio.sleep(1.5)  # Wait 1.5 seconds before cancelling
    for task in tasks:
        task.cancel()# Cancel all asynchronous tasks

# Main function
async def main():
    arr = [1, 2, 3]
    tasks = []
    results = []
    
    # Create the tasks and run async_map
    task = asyncio.create_task(async_map(arr, async_operation))
    tasks.append(task)
    
    # Start a task to cancel the operation after 1.5 seconds
    cancel_task = asyncio.create_task(cancel_operation(tasks))
    
    # Wait for all tasks to finish
    await asyncio.gather(task, cancel_task)
    
    # Print the results after cancellation
    print(f"Results: {results}")

# Run the main function
asyncio.run(main())