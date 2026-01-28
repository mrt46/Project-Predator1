# CLAUDE.md — AI Assistant Guide for Project Predator

## Project Overview

**Project Predator** is an autonomous cryptocurrency trading system built on a multi-agent architecture. It targets Binance USDT pairs and follows a phased development plan with strict risk governance. The system is currently in **Phase 3** (event-driven agent pipeline with fake data).

**Core philosophy:** Capital survival over profit. Risk controls always override signals. No single agent has full control. Every strategy must be replaceable at runtime.

**Current state:** Phase 3 of 7+ — EventBus-based agent communication with simulated market data. No live exchange connectivity, no database, no tests yet.

---

## Repository Structure

```
Project-Predator1/
├── backend/                          # Application source code
│   ├── main.py                       # FastAPI entry point, agent lifecycle
│   ├── core/
│   │   ├── engine.py                 # CoreEngine FSM (INIT→IDLE→RUNNING→HALTED)
│   │   └── logging.py               # Centralized logging setup
│   ├── config/
│   │   └── settings.py              # Environment-based settings
│   ├── agents/                       # Agent implementations
│   │   ├── base.py                  # BaseAgent abstract class
│   │   ├── strategist.py            # Strategist MCP — strategy evaluation
│   │   ├── market_scanner.py        # Market Scanner — coin discovery
│   │   ├── portfolio_manager.py     # Portfolio Manager — capital allocation
│   │   ├── cro.py                   # CRO — risk governance (veto authority)
│   │   ├── compliance.py            # Compliance — rule enforcement
│   │   ├── developer.py             # Developer MCP — maintenance/recovery
│   │   └── sentinel.py              # RRS — rate limiting & resources
│   ├── events/
│   │   └── bus.py                   # EventBus singleton (publish/subscribe)
│   └── data/
│       └── fake_market.py           # Simulated BTCUSDT/ETHUSDT tick feed
├── docker/
│   └── Dockerfile                   # Python 3.11-slim, FastAPI + Uvicorn
├── docker-compose.yml               # Single service on port 8000
├── docs/
│   ├── architecture/                # Phase 4 paper trading specs
│   └── policies/                    # Locked governance policies (9 files)
│       ├── RiskManagement.md        # Kill-switch types, drawdown rules
│       ├── StrategyGovernance.md    # Multi-strategy scoring model
│       ├── InvestmentPolicy.md
│       ├── LeveragePolicy.md
│       ├── AutonomyLevels.md
│       ├── ExchangePolicy.md
│       ├── InfrastructurePolicy.md
│       ├── ProductizationPolicy.md
│       └── DataAndLearningPolicy.md
├── CursorRules.md                   # Execution discipline + system architecture
├── Gunluk.md                        # Operations journal (Turkish)
├── AGENT DATA FLOW MAP/ADFM.md     # Canonical data flow rules (Turkish)
├── 7-DAY PHASED DEVELOPMENT PLAN/  # Phase roadmap
└── [12 Agent Specification .md files in root]
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| Framework | FastAPI |
| Server | Uvicorn (0.0.0.0:8000) |
| Async | asyncio (all I/O must be async) |
| Communication | In-process EventBus (Redis planned) |
| Container | Docker (python:3.11-slim) |
| Orchestration | docker-compose v3.9 |

**Not yet integrated (planned):** SQLite/PostgreSQL, Redis, ccxt.pro, pandas-ta, numpy, React frontend.

---

## Architecture

### Agent Pipeline

The system uses 12 specialized agents. Current execution flow:

```
Raw Market Data → Market Scanner → Strategist MCP → CRO (veto) →
Portfolio Manager → Execution/Trader → KPI Analyst → Human Observation
```

Any veto by CRO, Compliance, or risk controls immediately halts the signal.

### Authority Hierarchy (highest to lowest)

1. Human Operator
2. Compliance Agent
3. CRO / Risk Agent
4. Portfolio Manager
5. CursorRules.md / ADFM.md
6. Policy documents
7. Agent specifications
8. Generated code

### CoreEngine States

`INIT` → `IDLE` → `RUNNING` → `HALTED`

The engine runs a heartbeat every 5 seconds and transitions through these states during the application lifecycle.

### Event System

Events flow through a singleton `EventBus` (`backend/events/bus.py`):

- **Publish:** `await event_bus.publish("EVENT_TYPE", {"key": "value"})`
- **Subscribe:** `event_bus.subscribe("EVENT_TYPE", async_handler)`
- All handlers are async: `async def handler(payload: dict)`

Current event types:
- `MARKET_TICK` — published by FakeMarketDataFeed every 3 seconds
- `STRATEGY_SIGNAL` — published by StrategistAgent after evaluating a tick

---

## Development Workflow

### Running Locally

```bash
docker-compose up --build
```

The app starts on port 8000. Health check: `GET /health`.

### Verification Checklist

After any change, verify:
- `docker-compose up --build` succeeds
- `/health` endpoint responds with `{"status": "ok", ...}`
- Logs show heartbeat messages every 5 seconds
- Graceful shutdown works (Ctrl+C)
- No unauthorized agent activity in logs

### Git Conventions

- **Commit style:** Conventional commits with phase prefix
  - `feat(phase3): add event-driven agent pipeline`
  - `fix(phase2): correct agent lifecycle order`
- **Branch:** Development happens on feature branches
- **Deploy:** `git pull && docker-compose up --build -d`

### Phase Progression

| Phase | Description | Status |
|-------|------------|--------|
| FAZ 1 | Core engine skeleton, FastAPI, Docker | Complete |
| FAZ 2 | Agent skeletons with lifecycle logging | Complete |
| FAZ 3 | Event-driven architecture, fake data flow | **Current** |
| FAZ 4 | Paper trading engine with simulation | Next |
| FAZ 5 | Sandbox trading (real exchange, read-only) | Planned |
| FAZ 6 | Stability gate (pass/fail decision) | Planned |
| FAZ 7+ | Live trading (human approval required) | Planned |

---

## Code Conventions

### Naming

- **Classes:** PascalCase — `CoreEngine`, `EventBus`, `BaseAgent`
- **Functions/methods:** snake_case — `setup_logging`, `on_market_tick`
- **Constants:** SCREAMING_SNAKE_CASE — `PROJECT_NAME`, `EngineState.INIT`
- **Modules:** snake_case — `fake_market.py`, `portfolio_manager.py`
- **Agent NAME class attribute:** SCREAMING_SNAKE_CASE — `"STRATEGIST_MCP"`, `"CRO_RISK_MANAGER"`

### Agent Pattern

All agents extend `BaseAgent` and follow this structure:

```python
from .base import BaseAgent
from events.bus import event_bus
import logging

logger = logging.getLogger("predator-agent.{name}")

class SomeAgent(BaseAgent):
    NAME = "AGENT_NAME"

    async def start(self):
        await super().start()
        event_bus.subscribe("EVENT_TYPE", self.on_event)

    async def on_event(self, payload: dict):
        logger.info(f"[TAG] Processing: {payload}")
        # Process and optionally publish new events
        await event_bus.publish("OUTPUT_EVENT", result)

    async def stop(self):
        await super().stop()
```

### Logging

- Logger names: `"predator-{module}"` (e.g., `"predator-core.engine"`, `"predator-agent.strategist"`)
- Format: `%(asctime)s | %(levelname)s | %(name)s | %(message)s`
- Use bracketed tags in messages: `[INIT]`, `[START]`, `[STOP]`, `[STRATEGY]`, `[SCAN]`
- Log level: INFO for standard operations, WARNING for halts/errors

### Lifecycle

All components follow the same pattern:
- `async def start()` — initialize, subscribe to events
- `async def stop()` — cleanup, set `_running = False`
- FastAPI hooks: `@app.on_event("startup")` / `@app.on_event("shutdown")`

### Async Rules

- ALL I/O must use `async/await`
- Blocking calls are **forbidden**
- Long-running tasks use `asyncio.create_task()`

---

## Forbidden Actions

These are architectural constraints that must never be violated:

### Data Flow Prohibitions
- Strategist must NEVER send directly to Execution (must go through CRO)
- Oracle must NEVER connect to Portfolio Manager
- KPI Analyst must NEVER make decisions or recommendations
- Execution must NEVER provide learning feedback to strategies
- No agent may bypass Compliance override

### Agent Role Boundaries
- **Strategist:** Cannot execute trades, set risk rules, or allocate capital
- **Market Scanner:** Cannot generate signals or execute trades
- **CRO:** Cannot generate strategies; can only APPROVE/VETO
- **Portfolio Manager:** Cannot define risk parameters or control execution timing
- **Execution/Trader:** Cannot access strategy logic or learning systems
- **KPI Analyst:** Read-only measurement, no decisions

### System Rules
- Architecture defined in CursorRules.md / ADFM.md is **immutable**
- Never add or remove agents without explicit instruction
- Never alter the communication flow between agents
- Policy documents in `docs/policies/` are **locked** — do not modify
- If instructions are ambiguous, **stop and ask** rather than assume

---

## Key Files to Understand

| File | Purpose |
|------|---------|
| `backend/main.py` | Application entry point, agent registration, lifecycle hooks |
| `backend/core/engine.py` | CoreEngine state machine with heartbeat |
| `backend/events/bus.py` | EventBus pub/sub singleton — all agent communication |
| `backend/agents/base.py` | BaseAgent abstract class (start/stop lifecycle) |
| `backend/agents/strategist.py` | Only agent with meaningful logic (evaluates ticks, emits signals) |
| `backend/data/fake_market.py` | Phase 3 simulated market feed |
| `CursorRules.md` | Execution discipline, architecture spec, role definitions |
| `AGENT DATA FLOW MAP/ADFM.md` | Canonical data flow rules and forbidden paths |
| `docs/policies/RiskManagement.md` | Kill-switch types, drawdown ladder |
| `docs/policies/StrategyGovernance.md` | Strategy scoring model (weights, thresholds) |

---

## Risk Rules (Quick Reference)

### Drawdown Ladder (enforced, no exceptions)

| Daily Drawdown | Action |
|---------------|--------|
| >= 2% | Reduce Kelly by 50% |
| >= 3% | Disable all new trades |
| >= 4% | Tighten all trailing stops |
| >= 5% | Kill switch + 12h system halt |

### Strategy Score Formula

```
StrategyScore = 0.35 * Performance + 0.20 * Stability +
                0.25 * Regime + 0.10 * Risk + 0.10 * Freshness
```

### Position Sizing

Kelly criterion is used for sizing with mandatory caps:
- Must be fractional and regime-aware
- Max effective Kelly capped at 0.25
- If DrawdownFactor = 0, no new trades allowed

---

## Testing

**No tests exist yet.** There is no pytest configuration, test directory, or CI/CD pipeline. Validation is currently manual via the verification checklist above.

---

## Documentation Language

- **Code:** English
- **Documentation:** Mix of English (agent specs, policies) and Turkish (operations journal `Gunluk.md`, data flow map `ADFM.md`, phase plan)
- **Agent spec files:** 12 markdown files in the repository root, all in English

---

## Common Tasks

### Adding a new event type

1. Define the event name as a constant string (e.g., `"RISK_ALERT"`)
2. Have the publishing agent call `await event_bus.publish("RISK_ALERT", payload)`
3. Have subscribing agents call `event_bus.subscribe("RISK_ALERT", self.handler)` in their `start()` method
4. Verify the data flow is permitted by ADFM.md

### Adding behavior to a skeletal agent

Most agents (CRO, Portfolio Manager, Compliance, Developer, Sentinel) are currently skeletal — they only have `NAME` and inherit lifecycle from `BaseAgent`. To add behavior:

1. Import `event_bus` from `events.bus`
2. Override `start()` with `await super().start()` and subscribe to events
3. Add handler methods following the `async def on_{event}(self, payload: dict)` pattern
4. Respect the agent's role boundaries from its specification document

### Registering a new agent

1. Create the agent class in `backend/agents/` extending `BaseAgent`
2. Import and instantiate it in `backend/main.py`
3. Add it to the `agents` list
4. It will automatically start/stop with the application lifecycle
