from .base import BaseAgent
import logging
from .base import BaseAgent
from events.bus import event_bus

logger = logging.getLogger("predator-agent.scanner")

class MarketScannerAgent(BaseAgent):
    NAME = "MARKET_SCANNER"

    async def start(self):
        await super().start()
        event_bus.subscribe("MARKET_TICK", self.on_market_tick)

    async def on_market_tick(self, payload: dict):
        logger.info(f"[SCAN] Market tick received: {payload}") 
