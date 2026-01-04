import asyncio
from enum import Enum
import logging

logger = logging.getLogger("predator-core.engine")

class EngineState(str, Enum):
    INIT = "INIT"
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    HALTED = "HALTED"

class CoreEngine:
    def __init__(self):
        self.state = EngineState.INIT
        self._running = False

    async def start(self):
        logger.info("CoreEngine starting")
        self.state = EngineState.IDLE
        self._running = True
        asyncio.create_task(self._heartbeat())

    async def _heartbeat(self):
        while self._running:
            logger.info(f"Heartbeat | state={self.state}")
            await asyncio.sleep(5)

    async def halt(self):
        logger.warning("CoreEngine halting")
        self.state = EngineState.HALTED
        self._running = False
