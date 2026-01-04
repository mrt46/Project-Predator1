#############################################
# FILE: Gunluk.md
#############################################

# 🦁 PROJECT PREDATOR v2.9 – SYSTEM JOURNAL & OPERATION LOG

> This document is the **single source of truth**
> for operational history, decisions, incidents,
> and system-level learning.
>
> Logs are not noise.
> Logs are memory.

================================================
## 0. METADATA
================================================

- Project: PROJECT PREDATOR
- Version: v2.9
- Environment: (paper / live)
- Exchange: Binance
- Base Currency: USDT
- Vault Currency: BTC
- Start Date: YYYY-MM-DD
- Operator: Human Overseer (Read-Only)

================================================
## 1. DAILY SYSTEM SUMMARY
================================================

### Date: YYYY-MM-DD

- System Status: (ACTIVE / HALTED / RECOVERY)
- Market Regime: (Low Vol / Normal / High Vol / Extreme)
- Volatility Metrics:
  - ATR (14): 
  - σ (Rolling):
- News/Sentiment Bias:
  - Global: (Positive / Neutral / Negative)
  - Confidence Score: [0.0 – 1.0]

Explanation:
This section provides a high-level snapshot of the day.
It must be readable in under 60 seconds.

------------------------------------------------
### Capital & Risk Snapshot
------------------------------------------------

- Starting Equity:
- Ending Equity:
- Daily PnL (%):
- Daily Drawdown (%):
- Max Intraday Drawdown (%):
- Adaptive Kelly Multiplier:
- New Trades Allowed: (YES / NO)

------------------------------------------------
### Vault Status
------------------------------------------------

- Vault Balance (BTC):
- Vault Balance (USD equiv):
- Profit Skimmed Today:
- Vault Sweep Flag: (NONE / SCHEDULED / COMPLETED)

================================================
## 2. STRATEGY ACTIVITY LOG
================================================

### Strategy: <strategy_name>

- Status: (ACTIVE / PAPER / DISABLED)
- Regime Compatibility: (Low / Normal / High Vol)
- Entry Logic Summary:
- Exit Logic Mode: (Trailing / ROI / Emergency)
- Adaptive Kelly Applied: YES / NO

#### Trades Executed

| Time (UTC) | Pair | Side | Size | Entry | Exit | PnL % | Exit Reason |
|-----------|------|------|------|-------|------|-------|-------------|

Explanation:
Every trade must have a clear exit reason.
“No reason” is not acceptable.

================================================
## 3. RISK ENGINE DECISIONS
================================================

### Risk Events

- Drawdown Level Reached: (%)
- Action Taken:
  - Kelly Reduction
  - Trade Halt
  - Trailing Tighten
  - Kill Switch

### Notes
- Reasoning:
- Was this expected? (YES / NO)
- Did risk override a signal? (YES / NO)

================================================
## 4. ORACLE & SENTINEL INTELLIGENCE
================================================

### News Summary
- Key Events:
- Impact Assessment: (LOW / MEDIUM / HIGH)

### Sentiment Analysis
- Source Signals:
  - Twitter
  - News
  - Market Anomalies
- Sentiment Score:
- Applied Risk Modifier:

Explanation:
Sentiment entries are for CONTEXT.
They must never be interpreted as direct signals.

================================================
## 5. EXECUTION & INFRASTRUCTURE
================================================

### Exchange Connectivity
- WebSocket Status: (STABLE / DEGRADED / DISCONNECTED)
- API Rate Limits Hit: (YES / NO)
- Slippage Events: (NONE / MINOR / MAJOR)

### Order Execution Notes
- Limit vs Market Ratio:
- Failed Orders:
- Retries:

================================================
## 6. DEVELOPER MCP ACTIVITY
================================================

### Errors Detected
- Timestamp:
- Module:
- Error Summary:
- Severity: (LOW / MEDIUM / HIGH / CRITICAL)

### Self-Healing Workflow
- Phase Reached:
  - OBSERVE
  - PROPOSE
  - EXECUTE
- Patch Applied: (YES / NO)
- Canary Result: (PASS / FAIL)

Explanation:
Any automatic fix MUST be traceable here.
If it is not logged here, it did not happen.

================================================
## 7. BLACK SWAN & EXCEPTION EVENTS
================================================

### Trigger
- Type:
  - Price Gap
  - Exchange Failure
  - Liquidity Collapse
- Threshold Breached:

### System Response
- Positions Closed: (YES / NO)
- Trading Halt Duration:
- Post-Mortem Required: (YES / NO)

================================================
## 8. HUMAN OVERSIGHT NOTES (OPTIONAL)
================================================

> Read-only human observations.
> No operational commands allowed here.

- Observations:
- Concerns:
- Hypotheses:

================================================
## 9. POST-MORTEM (IF APPLICABLE)
================================================

### Incident Summary
- What happened:
- Root Cause:
- Detection Time:
- Response Time:

### Lessons Learned
- What failed:
- What worked:
- What must change:

### Action Items
- [ ] Strategy update
- [ ] Risk parameter adjustment
- [ ] Infrastructure change
- [ ] No action needed

================================================
## 10. END-OF-DAY SIGN-OFF
================================================

- System Health Assessment: (STABLE / DEGRADED / AT RISK)
- Confidence in Edge: (HIGH / MEDIUM / LOW)
- Ready for Next Session: (YES / NO)

Signed:
- System: PROJECT PREDATOR
- Timestamp: YYYY-MM-DD HH:MM UTC

================================================
# END OF FILE
================================================

#############################################
# FILE: Gunluk.md (ROLE-SPECIFIC EXTENSIONS)
#############################################

================================================
## 11. CHIEF RISK OFFICER (CRO) – RISK OVERSIGHT LOG
================================================

> This section records ALL CRO decisions.
> CRO logs are authoritative and override performance metrics.

### CRO Daily Risk Snapshot
- Date:
- Global Risk Level: (LOW / MODERATE / HIGH / CRITICAL)
- Max Allowed Portfolio Exposure (%):
- Max Single Strategy Exposure (%):
- Max Leverage Allowed: (if applicable)

### CRO Decisions Today
For each decision, ONE entry is mandatory.

- Timestamp (UTC):
- Decision Type:
  - Strategy Approval
  - Strategy Rejection
  - Exposure Cap
  - Forced De-Risk
  - Emergency Kill Switch
- Affected Scope:
  - Global
  - Strategy Name
  - Asset / Pair
- Reason Category:
  - Excess Volatility
  - Correlation Risk
  - Drawdown Escalation
  - Liquidity Risk
  - Black Swan Trigger
- Decision Rationale (Short, Factual):
- Was this a VETO? (YES / NO)

Explanation:
CRO decisions are logged without justification bias.
Outcome (profit/loss) MUST NOT affect wording.
This log exists to prove risk discipline, not intelligence.

================================================
## 12. PORTFOLIO MANAGER (PM) – ALLOCATION & CORRELATION LOG
================================================

> This section documents portfolio-level decisions.
> PM does not judge signals, only portfolio impact.

### Portfolio State Snapshot
- Total Active Strategies:
- Portfolio Gross Exposure (%):
- Portfolio Net Exposure (%):
- Largest Strategy Allocation (%):
- Correlation Risk Level: (LOW / MEDIUM / HIGH)

### Strategy Allocation Changes
Log EACH change separately.

- Timestamp (UTC):
- Strategy Name:
- Previous Allocation (%):
- New Allocation (%):
- Change Type:
  - Increase
  - Reduction
  - Freeze
  - Reactivation
- Reason:
  - High Correlation
  - Sector Concentration
  - Drawdown Control
  - Capital Rebalancing
- Correlation Affected:
  - YES / NO
  - If YES, Correlated Strategies:

Explanation:
The PM log explains WHY capital moved,
not whether the move was profitable.
Correlation control is the primary objective.

================================================
## 13. COMPLIANCE & RULE ENFORCEMENT LOG
================================================

> This section is legally and operationally critical.
> If it is not logged here, it did not happen.

### Compliance Checks Summary
- Total Trades Reviewed:
- Trades Blocked:
- Active Rule Set Version:
- Compliance Status: (CLEAR / WARNING / BREACH)

### Rule Violations & Vetoes
Each violation MUST be logged immediately.

- Timestamp (UTC):
- Trade / Strategy ID:
- Rule Violated:
  - CursorRules.md Section:
  - Mimari.md Section:
- Violation Type:
  - Architecture Breach
  - Risk Rule Violation
  - Unauthorized Parameter Change
  - Execution Flow Bypass
- Action Taken:
  - Trade Blocked
  - Strategy Frozen
  - System Halt Requested
- Escalated to Human Operator? (YES / NO)

Explanation:
Compliance does not negotiate.
A profitable violation is still a violation.
This log protects the system from silent drift.

================================================
## 14. MULTI-ROLE VETO TRACE (MANDATORY IF ANY VETO OCCURS)
================================================

> This section is required whenever a trade is NOT executed
> due to CRO, PM, or Compliance intervention.

### Veto Event Record
- Timestamp (UTC):
- Trade / Signal ID:
- Veto Issued By:
  - CRO
  - Portfolio Manager
  - Compliance
- Stage of Interruption:
  - Post-Signal
  - Post-Allocation
  - Pre-Execution
- Original Intended Action:
- Final Outcome: (EXECUTED / BLOCKED)

### Veto Rationale (Factual, No Opinion)
- Primary Reason:
- Secondary Factors (if any):

Explanation:
This section reconstructs “what would have happened”
versus “what was allowed to happen”.
It is essential for post-mortem analysis.

================================================
## 15. END-OF-DAY ROLE CONCURRENCE
================================================

> Each role must explicitly signal its end-of-day status.

- CRO Assessment:
  - Risk Acceptable for Next Session? (YES / NO)
- PM Assessment:
  - Portfolio Balanced? (YES / NO)
- Compliance Assessment:
  - Rules Fully Enforced? (YES / NO)

If ANY answer is NO:
→ System status MUST be set to DEGRADED or HALTED.

Signed (System Generated):
- CRO
- Portfolio Manager
- Compliance

================================================
# END OF ROLE-SPECIFIC EXTENSIONS
================================================
