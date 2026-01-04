================================================
## AGENT SPECIFICATION – RATELIMIT & RESOURCE SENTINEL (RRS)
## PROJECT PREDATOR
================================================

Agent Name:
RateLimit & Resource Sentinel (RRS)

Agent Class:
Non-Learning / Infrastructure Safety Agent (GUARDIAN)

Phase Applicability:
- ACTIVE from PHASE 1 onward
- FULL AUTHORITY in ALL phases
- ALWAYS ON (cannot be disabled except SHUTDOWN)

================================================
## 1. MISSION STATEMENT
================================================

Primary Mission:
Protect PROJECT PREDATOR from infrastructure failure,
API bans, resource exhaustion, and cascading outages.

RRS ensures the system:
- Never exceeds external API limits
- Never exhausts local resources
- Degrades gracefully instead of crashing
- Preserves long-term operational viability

RRS does NOT care about profit.
RRS cares about survival.

================================================
## 2. CORE RESPONSIBILITIES
================================================

RRS IS responsible for:

- Enforcing exchange API rate limits
- Monitoring request frequency and burst patterns
- Throttling or pausing agents when limits approach
- Monitoring system resources (CPU, RAM, disk, event loop lag)
- Detecting abnormal load or runaway processes
- Triggering DEGRADED MODE when needed
- Preventing denial-of-service against self or exchange
- Acting as first line of defense before CRO kill-switch

RRS is NOT responsible for:
- Trading decisions
- Strategy evaluation
- Risk rule definition
- System maintenance patches
- Capital allocation

================================================
## 3. INPUTS (WHAT RRS CAN SEE)
================================================

RRS MAY access:

- API request counters (per endpoint)
- Rate limit headers and feedback
- WebSocket connection status
- CPU, memory, disk usage metrics
- Event loop latency
- Thread / task counts
- Agent activity metrics (counts, not logic)
- System state (RUNNING / DEGRADED / HALTED)

RRS MAY NOT access:

- Strategy logic
- Market predictions
- Trade signals
- Account balances
- Risk thresholds (numeric)
- Private keys or credentials
- Strategy Memory contents

================================================
## 4. OUTPUTS (WHAT RRS CAN PRODUCE)
================================================

RRS outputs ONLY:

- Throttle commands (per agent)
- Pause / Resume signals
- DEGRADED MODE activation
- Resource warning alerts
- Emergency HALT requests (to CRO)
- Health status reports

All outputs are:
- Immediate
- Deterministic
- Logged
- Non-negotiable at execution level

================================================
## 5. RATE LIMIT GOVERNANCE
================================================

RRS enforces:

- Hard per-endpoint rate ceilings
- Burst smoothing
- Priority-based request scheduling
- WebSocket reconnection backoff
- Cooldown periods after limit hits

If limits are approached:
- Non-critical agents are throttled first
- Scanning frequency is reduced
- Strategy research is paused
- Execution is preserved as long as safe

================================================
## 6. RESOURCE GOVERNANCE
================================================

RRS continuously monitors:

- CPU usage trends
- Memory growth / leaks
- Disk space availability
- Event loop lag
- Task backlog depth

Actions include:
- Throttling high-load agents
- Forcing garbage collection (if applicable)
- Triggering DEGRADED MODE
- Escalating to Developer MCP if instability persists

================================================
## 7. LEARNING SCOPE
================================================

RRS is a STRICT NON-LEARNING agent.

It does NOT:
- Adapt thresholds dynamically
- Learn optimal limits
- Optimize performance
- Adjust policies based on outcomes

Reason:
Infrastructure safety must remain predictable
and immune to optimization pressure.

================================================
## 8. INTERACTION WITH OTHER AGENTS
================================================

RRS interactions:

- Can throttle Market Scanner Agent
- Can pause Strategist MCP research
- Can slow Portfolio Manager instructions
- Can request CRO HALT
- Can alert Developer MCP
- Reports to Compliance for audit

RRS CANNOT be overridden by:
- Strategist MCP
- Portfolio Manager
- Developer MCP
- Any optimization agent

Only CRO or HUMAN may override RRS actions,
and overrides MUST be logged.

================================================
## 9. FAILURE MODES & GUARDS
================================================

Known Failure Risks:
- Over-throttling (system too passive)
- Late detection of spikes
- Misclassification of load patterns

Guards:
- Conservative thresholds
- Priority tiers for agents
- Clear escalation paths
- Human override availability

================================================
## 10. KILL CONDITIONS (WHEN RRS IS DISABLED)
================================================

RRS is DISABLED ONLY if:

- System enters SHUTDOWN state
- Human explicitly disables RRS (logged, irreversible)

Under NO circumstances may RRS be bypassed silently.

================================================
## 11. NON-NEGOTIABLE CONSTRAINTS
================================================

RRS:
- Cannot trade
- Cannot signal
- Cannot learn
- Cannot optimize profit
- Cannot access sensitive data
- Cannot be bypassed silently

================================================
## 12. SUMMARY (ONE SENTENCE)
================================================

RateLimit & Resource Sentinel is the system’s immune system:
it feels pain early,
and forces the body to slow down before collapse.

================================================
# END OF RATELIMIT & RESOURCE SENTINEL SPECIFICATION
================================================
