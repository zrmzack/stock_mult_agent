# Crypto Alpha Agent

AI-powered BTC / ETH market intelligence platform.

> This project is not an auto-trading bot. It is an explainable crypto market analysis system that generates probability-based outlooks, risk warnings, and scenario analysis.

## 1. Project Vision

Crypto Alpha Agent aims to answer four practical questions:

1. Why is BTC / ETH rising or falling?
2. What is the current market regime?
3. What is the probability of upward / sideways / downward movement over the next 3, 7, and 14 days?
4. What are the key risks and alternative scenarios?

The system should not output deterministic price predictions such as `BTC = 150000`. It should output probability distributions such as:

```json
{
  "asset": "BTC",
  "horizon": "7d",
  "up_probability": 0.66,
  "sideways_probability": 0.22,
  "down_probability": 0.12,
  "market_regime": "institution_driven_bull",
  "confidence": 0.72
}
```

## 2. MVP Scope

The first version should focus on BTC only. ETH can be added after the BTC pipeline is stable.

### MVP Features

- BTC market data collection
- Macro data collection
- ETF flow analysis
- Derivatives flow analysis
- Market regime detection
- Alpha score generation
- 3 / 7 / 14 day probability outlook
- Explainable report generation
- Risk warning generation
- Scenario analysis
- REST API service

### Deferred Features

- ETH-specific analysis
- Stablecoin Agent
- Policy Agent
- News Agent with LLM-based sentiment
- Dashboard frontend
- Backtesting UI
- Telegram / email alerts

## 3. High-Level Architecture

```text
Data Layer
  -> Agent Layer
  -> Judge Agent
  -> Prediction Engine
  -> Risk Engine
  -> Explain Engine
  -> Scenario Engine
  -> Report API
```

## 4. Core Agents

| Agent | Purpose | MVP |
|---|---|---|
| Macro Agent | Analyze DXY, Nasdaq, rates, Treasury yields | Yes |
| ETF Agent | Analyze BTC / ETH ETF flows | Yes for BTC |
| Flow Agent | Analyze OI, funding, liquidation, volume | Yes |
| Regime Agent | Identify market state | Yes |
| Judge Agent | Fuse scores and apply dynamic weights | Yes |
| Prediction Engine | Convert alpha score into probabilities | Yes |
| Explain Agent | Explain why the system is bullish / bearish | Yes |
| Scenario Agent | Generate bullish / neutral / bearish scenarios | Yes |
| Stablecoin Agent | Analyze crypto liquidity via USDT / USDC | Later |
| News Agent | Analyze sentiment from RSS / news | Later |
| Policy Agent | Analyze regulatory events | Later |

## 5. Development Principles

- Build analysis, not auto-trading.
- Use probability, not deterministic prediction.
- Explain every signal and every prediction.
- Store all inputs, scores, and outputs for auditability.
- Keep all weights configurable.
- Start simple with rule-based scoring, then add models after enough data is collected.

## 6. Repository Documents

- `AGENTS.md`: AI coding agent rules and repository conventions
- `ARCHITECTURE.md`: system architecture
- `TASKS.md`: Codex task breakdown
- `PREDICTION_ENGINE.md`: probability engine design
- `DATA_SOURCES.md`: free and low-cost data sources
- `API_SPEC.md`: REST API design

## 7. Disclaimer

This project provides market analysis only. It does not provide financial advice, investment recommendations, or automated trading execution.
