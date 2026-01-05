from fastapi import FastAPI
import logging

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

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")
    await engine.start()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")
    await engine.halt()

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "engine_state": engine.state,
    }
    
@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")
    await engine.start()
    for agent in agents:
        await agent.start()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")
    for agent in agents:
        await agent.stop()
    await engine.halt()
