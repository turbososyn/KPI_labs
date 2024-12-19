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