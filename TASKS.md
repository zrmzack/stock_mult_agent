# TASKS.md

## Development Strategy

Start with BTC only. Build a working end-to-end analysis pipeline before adding ETH or advanced agents.

## Sprint 0: Project Foundation

- Task-001: Initialize repository structure: backend, agents, collectors, database, scheduler, tests, docs.
- Task-002: Add Python project config: pyproject.toml, requirements or uv config, .env.example, .gitignore.
- Task-003: Add Docker Compose with backend, postgres, redis.
- Task-004: Create FastAPI app with /api/v1/health and /api/v1/version.
- Task-005: Add structured JSON logging.

## Sprint 1: Database Layer

- Task-006: Define SQLAlchemy models for market_snapshot, agent_score, prediction_result, risk_result, scenario_result, news_event, market_regime.
- Task-007: Add Alembic migrations.
- Task-008: Add database session management.

## Sprint 2: Market Data Collectors

- Task-009: Gate ticker collector.
- Task-010: Gate funding collector.
- Task-011: Gate open interest collector.
- Task-012: Gate K-line collector.
- Task-013: Binance fallback collector.
- Task-014: Market snapshot builder.

## Sprint 3: Macro Agent

- Task-015: Macro data collector.
- Task-016: Macro scoring logic.
- Task-017: Macro Agent API.
- Task-018: Macro Agent tests.

## Sprint 4: ETF Agent

- Task-019: ETF data schema.
- Task-020: BTC ETF collector.
- Task-021: ETF rolling metrics.
- Task-022: ETF scoring logic.
- Task-023: ETF Agent tests.

## Sprint 5: Flow Agent

- Task-024: Funding analyzer.
- Task-025: Open interest analyzer.
- Task-026: Liquidation analyzer placeholder.
- Task-027: Flow scoring logic.
- Task-028: Flow Agent tests.

## Sprint 6: Regime Agent

- Task-029: Define regime enum.
- Task-030: Regime detection rules.
- Task-031: Regime confidence logic.
- Task-032: Regime Agent tests.

## Sprint 7: Judge Agent

- Task-033: Add weight configuration.
- Task-034: Implement score fusion.
- Task-035: Store judge result.
- Task-036: Judge Agent tests.

## Sprint 8: Prediction Engine

- Task-037: Implement probability mapping.
- Task-038: Implement time decay.
- Task-039: Implement risk adjustment.
- Task-040: Store prediction result.
- Task-041: Prediction Engine tests.

## Sprint 9: Risk Engine

- Task-042: Define risk factors.
- Task-043: Implement risk scoring.
- Task-044: Risk API.
- Task-045: Risk Engine tests.

## Sprint 10: Explain Engine

- Task-046: Driver extraction.
- Task-047: Risk explanation.
- Task-048: Human-readable report text.
- Task-049: Explain Engine tests.

## Sprint 11: Scenario Engine

- Task-050: Scenario schema.
- Task-051: Generate bullish scenario.
- Task-052: Generate sideways scenario.
- Task-053: Generate bearish scenario.
- Task-054: Scenario probability normalization.
- Task-055: Scenario API.

## Sprint 12: Report API

- Task-056: BTC report endpoint.
- Task-057: Market report endpoint.
- Task-058: Latest snapshot endpoint.
- Task-059: API tests.

## Sprint 13: Scheduler

- Task-060: Add scheduled collectors.
- Task-061: Add scheduled agent runs.
- Task-062: Add scheduled report generation.

## Sprint 14: Backtesting Foundation

- Task-063: Historical snapshot query.
- Task-064: Prediction outcome evaluator.
- Task-065: Backtest metrics.

## Sprint 15: MVP Hardening

- Task-066: Add exception handling.
- Task-067: Add data freshness checks.
- Task-068: Add README run instructions.
- Task-069: Add CI workflow.
- Task-070: MVP release tag.
