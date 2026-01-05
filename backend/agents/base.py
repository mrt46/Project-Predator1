import logging

logger = logging.getLogger("predator-agent")

class BaseAgent:
    NAME = "BASE_AGENT"

    def __init__(self):
        logger.info(f"[INIT] {self.NAME}")

    async def start(self):
        logger.info(f"[START] {self.NAME}")

    async def stop(self):
        logger.info(f"[STOP] {self.NAME}")

