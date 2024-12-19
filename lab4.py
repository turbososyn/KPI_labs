import asyncio

# Let's create an asynchronous generator for iteration over a large data set
async def async_data_generator(start, end):
    for i in range(start, end):
        await asyncio.sleep(0.1) # Simulate asynchronous loading or processing
        yield i # We return the element one at a time

# Asynchronous function for processing data
async def process_data(start, end, filename):
    async for data in async_data_generator(start, end):
       # Processing of each element (for example, we multiply by 2)
        result = data * 2
        # Write the result to a file
        with open(filename, 'a') as f:
            f.write(f"{data} -> {result}\n")
        print(f"Processed: {data} -> {result}")

# Main asynchronous function to start processing
async def main():
    filename = "processed_data.txt"
    start = 1
    end = 101 # For example, we process numbers from 1 to 100
    
    # First, let's clean the file
    open(filename, 'w').close()
    
    # Start processing
    await process_data(start, end, filename)

# We start an asynchronous cycle
if __name__ == "__main__":
    asyncio.run(main())