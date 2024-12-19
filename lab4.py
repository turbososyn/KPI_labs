import asyncio
async def async_data_generator(start, end):
    for i in range(start, end):
        await asyncio.sleep(0.1) 
        yield i 
async def process_data(start, end, filename):
    async for data in async_data_generator(start, end):
        result = data * 2
        with open(filename, 'a') as f:
            f.write(f"{data} -> {result}\n")
        print(f"Processed: {data} -> {result}")
async def main():
    filename = "processed_data.txt"
    start = 1
    end = 101
    open(filename, 'w').close()
    await process_data(start, end, filename)
if __name__ == "__main__":
    asyncio.run(main())