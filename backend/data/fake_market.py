
import asyncio
import logging
import random

from events.bus import event_bus

logger = logging.getLogger("predator-fake-market")

class FakeMarketDataFeed:
    def __init__(self, symbols=None):
        self.symbols = symbols or ["BTCUSDT", "ETHUSDT"]
        self.running = False

    async def start(self):
        logger.info("FakeMarketDataFeed started")
        self.running = True
        while self.running:
            symbol = random.choice(self.symbols)
            price = round(random.uniform(1000, 60000), 2)

            await event_bus.publish(
                event_type="MARKET_TICK",
                payload={
                    "symbol": symbol,
                    "price": price,
                },
            )

            await asyncio.sleep(3)

    async def stop(self):
        logger.info("FakeMarketDataFeed stopped")
        self.running = False