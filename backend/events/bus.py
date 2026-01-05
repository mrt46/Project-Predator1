import logging
from collections import defaultdict

logger = logging.getLogger("predator-event-bus")

class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event_type: str, handler):
        logger.info(f"Subscribed to event: {event_type}")
        self.subscribers[event_type].append(handler)

    async def publish(self, event_type: str, payload: dict):
        logger.info(f"Event published: {event_type} | payload={payload}")
        for handler in self.subscribers[event_type]:
            await handler(payload)


event_bus = EventBus()
