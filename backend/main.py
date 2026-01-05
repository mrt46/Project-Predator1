from fastapi import FastAPI
import logging
import asyncio

from core.engine import CoreEngine
from core.logging import setup_logging
from config.settings import PROJECT_NAME

from agents.strategist import StrategistAgent
from agents.market_scanner import MarketScannerAgent
from agents.cro import CROAgent
from agents.portfolio_manager import PortfolioManagerAgent
from agents.compliance import ComplianceAgent
from agents.developer import DeveloperAgent
from agents.sentinel import SentinelAgent

from data.fake_market import FakeMarketDataFeed

logger = setup_logging()

app = FastAPI(title=PROJECT_NAME)

engine = CoreEngine()

agents = [
    StrategistAgent(),
    MarketScannerAgent(),
    CROAgent(),
    PortfolioManagerAgent(),
    ComplianceAgent(),
    DeveloperAgent(),
    SentinelAgent(),
]

fake_market = FakeMarketDataFeed()

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")

    await engine.start()

    for agent in agents:
        await agent.start()

    # FAZ 3 ONLY – fake data feed
    asyncio.create_task(fake_market.start())

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")

    await fake_market.stop()

    for agent in agents:
        await agent.stop()

    await engine.halt()

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "engine_state": engine.state,
    }