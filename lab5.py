import asyncio
import time

# Observable class to handle message communication
class Observable:
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, callback):
        """Subscribe a listener to the observable."""
        self.subscribers.append(callback)
    
    async def notify(self, message):
        """Notify all subscribers with the new message."""
        # Notify each subscriber (which should be an async function)
        for subscriber in self.subscribers:
            # Wrap the subscriber call in awaitable
            await subscriber(message)

# Simulate an entity sending messages asynchronously
async def send_message(observable, message):
    print(f"Sending message: {message}")
    await observable.notify(message)

# Simulate an entity subscribing to messages and processing them
async def message_listener(name, queue, log_file):
    while True:
        # Wait for the next message
        message = await queue.get()# Get the message from the queue
        if message is None:
            break # Stop if we receive a None message (shutdown signal)
        
        print(f"{name} received message: {message}")
        
        # Log the received message to a file
        with open(log_file, 'a') as f:
            f.write(f"{name} processed message: {message} at {time.ctime()}\n")
        
         # Simulating some async processing time
        await asyncio.sleep(1)

async def main():
    # Create an observable object
    observable = Observable()
    
    # Log file where messages will be saved
    log_file = 'messages.log'
    
   # Create a queue for message passing
    queue = asyncio.Queue()
    
    # Create two subscribers (listeners) with separate queues
    listener_1 = asyncio.create_task(message_listener("Listener 1", queue, log_file))
    listener_2 = asyncio.create_task(message_listener("Listener 2", queue, log_file))
    
    # Subscribe listeners to the observable with an async function to put messages in the queue
    observable.subscribe(lambda message: asyncio.create_task(queue.put(message)))
    
    # Send some messages
    await send_message(observable, "Hello, world!")
    await send_message(observable, "This is a test message")
    await send_message(observable, "Another test message")
    
    # Add a stop signal to the queue (None is used as a signal to stop the listener tasks)
    await queue.put(None) # Stop listener 1
    await queue.put(None) # Stop listener 2
    
    # Wait for the listeners to finish
    await asyncio.gather(listener_1, listener_2)

# Run the main asyncio event loop
if __name__ == '__main__':
    asyncio.run(main())