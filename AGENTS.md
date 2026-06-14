# AGENTS.md

This repository is designed for AI coding agents such as Codex, Cursor, Claude Code, or other coding assistants.

## 1. Project Objective

Build an AI-powered crypto market intelligence platform.

Do not build:

- auto trading
- trade execution
- high frequency trading
- wallet features

Build:

- market analysis
- probability forecasting
- explainability
- risk analysis
- scenario generation
- report APIs

## 2. Core Rule

Every conclusion must be explainable.

Bad output:

```json
{"up_probability": 0.67}
```

Good output:

```json
{
  "up_probability": 0.67,
  "reasons": [
    "ETF flow is positive",
    "DXY is weakening",
    "OI rises with price while funding remains moderate"
  ],
  "risks": [
    "Funding rate may become overheated"
  ]
}
```

## 3. Recommended Technology Stack

- Python 3.12+
- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Alembic
- Pydantic v2
- APScheduler or Celery beat
- pytest
- Docker Compose

## 4. Repository Layout

```text
backend/
  app/
    api/
    core/
    db/
    models/
    schemas/
    services/

agents/
  macro_agent/
  etf_agent/
  flow_agent/
  stablecoin_agent/
  news_agent/
  policy_agent/
  regime_agent/
  judge_agent/
  explain_agent/
  scenario_agent/

collectors/
  gate/
  binance/
  macro/
  etf/
  news/

database/
  migrations/
  seed/

scheduler/

tests/
  unit/
  integration/

docs/
```

## 5. Agent Output Contract

Every agent must output the following shape:

```json
{
  "agent_name": "macro_agent",
  "asset": "BTC",
  "score": 0,
  "trend": "bullish|neutral|bearish",
  "confidence": 0.0,
  "reasons": [],
  "risks": [],
  "raw_inputs": {},
  "timestamp": "ISO-8601"
}
```

## 6. Scoring Rules

- All scores must be normalized to 0-100.
- 0-40 means bearish.
- 40-60 means neutral.
- 60-80 means bullish.
- 80-100 means strongly bullish.
- No hardcoded final probabilities.
- All weights must come from configuration.

## 7. Configuration Rules

Use config files for:

- scoring weights
- data source URLs
- optional API credentials
- collection intervals
- risk thresholds
- regime thresholds

Do not hardcode magic numbers inside business logic.

## 8. Logging Rules

All agents must log:

- start time
- input source
- score result
- error message
- execution duration

Log format:

```json
{
  "timestamp": "ISO-8601",
  "agent": "flow_agent",
  "level": "INFO",
  "message": "flow score calculated",
  "duration_ms": 120
}
```

## 9. Database Rules

Never store predictions only. Always store:

- input snapshot
- agent scores
- weights used
- final alpha score
- probability output
- explanations
- risk factors

This is required for auditing and backtesting.

## 10. Testing Rules

Every agent must include:

- unit tests for scoring logic
- integration tests for API / database writes
- mock tests for external data collectors

A feature is not complete unless tests pass.

## 11. Security Rules

- Use read-only market data credentials when credentials are needed.
- Do not implement order placement unless explicitly approved in a future product document.
- Do not expose secrets in logs.

## 12. Definition of Done

A task is complete only when:

- code implemented
- tests added
- logs added
- config added if needed
- API documented if applicable
- database persistence added if applicable
- errors handled gracefully
