import asyncio
import time
class Observable:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, callback):
        """Subscribe a listener to the observable."""
        self.subscribers.append(callback)
    async def notify(self, message):
        """Notify all subscribers with the new message."""
        for subscriber in self.subscribers:
            await subscriber(message)
async def send_message(observable, message):
    print(f"Sending message: {message}")
    await observable.notify(message)
async def message_listener(name, queue, log_file):
    while True:
        message = await queue.get()
        if message is None:
            break 
        print(f"{name} received message: {message}")
        with open(log_file, 'a') as f:
            f.write(f"{name} processed message: {message} at {time.ctime()}\n")
        await asyncio.sleep(1)
async def main():
    observable = Observable()
    log_file = 'messages.log'
    queue = asyncio.Queue()
    listener_1 = asyncio.create_task(message_listener("Listener 1", queue, log_file))
    listener_2 = asyncio.create_task(message_listener("Listener 2", queue, log_file))
    observable.subscribe(lambda message: asyncio.create_task(queue.put(message)))
    await send_message(observable, "Hello, world!")
    await send_message(observable, "This is a test message")
    await send_message(observable, "Another test message")
    await queue.put(None) 
    await queue.put(None)
    await asyncio.gather(listener_1, listener_2)
if __name__ == '__main__':
    asyncio.run(main())