import logging
from .base import BaseAgent
from events.bus import event_bus

logger = logging.getLogger("predator-agent.strategist")

class StrategistAgent(BaseAgent):
    NAME = "STRATEGIST_MCP"

    async def start(self):
        await super().start()
        event_bus.subscribe("MARKET_TICK", self.on_market_tick)

    async def on_market_tick(self, payload: dict):
        logger.info(f"[STRATEGY] Evaluating payload: {payload}")

        fake_signal = {
            "symbol": payload["symbol"],
            "action": "BUY",
            "confidence": 0.42,
        }

        await event_bus.publish("STRATEGY_SIGNAL", fake_signal)