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
