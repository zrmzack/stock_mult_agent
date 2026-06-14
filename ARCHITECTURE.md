# ARCHITECTURE.md

## 1. System Overview

Crypto Alpha Agent is a modular market intelligence system.

```text
External Data Sources
        ↓
Collectors
        ↓
Raw Data Storage
        ↓
Feature Engineering
        ↓
Agent Layer
        ↓
Judge Agent
        ↓
Prediction Engine
        ↓
Risk / Explain / Scenario Engines
        ↓
REST API / Reports / Dashboard
```

## 2. Data Layer

The data layer collects and stores raw and processed market information.

### Main Categories

| Category | Example Data |
|---|---|
| Market Data | BTC price, ETH price, volume, K-lines |
| Derivatives | OI, funding, liquidation, long-short ratio |
| Macro | DXY, Nasdaq, rates, Treasury yields |
| ETF | BTC ETF flow, ETH ETF flow |
| Stablecoin | USDT / USDC supply and market cap |
| News | RSS articles, headlines, sentiment |
| Policy | SEC, ETF approval, MiCA, Hong Kong regulation |

## 3. Agent Layer

Each agent has one responsibility and outputs a normalized score.

### Macro Agent

Analyzes global liquidity and risk appetite.

Inputs:

- DXY
- Nasdaq
- Treasury yields
- Fed rate
- CPI calendar when available

Output:

- `macro_score`
- `macro_trend`
- reasons and risks

### ETF Agent

Analyzes institutional inflows and outflows.

Inputs:

- BTC spot ETF daily net flow
- ETH spot ETF daily net flow
- rolling 3-day and 7-day flows

Output:

- `etf_score`
- institutional flow trend

### Flow Agent

Analyzes derivatives positioning.

Inputs:

- Open interest
- Funding rate
- Liquidation data
- Price change
- Volume change

Output:

- `flow_score`
- squeeze risk
- funding risk

### Regime Agent

Identifies the current market state.

Possible regimes:

- `bull`
- `bear`
- `sideways`
- `risk_off`
- `short_squeeze`
- `long_liquidation`
- `news_driven`
- `institution_driven`

Output:

- `market_regime`
- `confidence`

### Judge Agent

Combines all agent scores using dynamic weights based on regime.

Output:

- `alpha_score`
- `score_breakdown`
- `selected_weights`

## 4. Prediction Layer

The prediction layer converts alpha scores into probability distributions.

Output horizons:

- 3 days
- 7 days
- 14 days

Each horizon outputs:

```json
{
  "up": 0.64,
  "sideways": 0.23,
  "down": 0.13
}
```

## 5. Risk Engine

Detects risk factors, including:

- ETF outflow streak
- overheated funding
- abnormal OI rise
- DXY rebound
- negative regulatory headlines
- high volatility before macro events

Output:

- `risk_score`
- `risk_level`
- `risk_reasons`

## 6. Explain Engine

Converts numeric outputs into human-readable explanations.

Must explain:

- why bullish
- why bearish
- why neutral
- what could invalidate the prediction

## 7. Scenario Engine

Generates three scenarios:

1. Bullish case
2. Base case / sideways case
3. Bearish case

Each scenario contains:

- probability
- trigger conditions
- expected market behavior
- risk factors

## 8. Report API

REST API returns full analysis output.

Main endpoints:

- `/api/v1/btc/report`
- `/api/v1/eth/report`
- `/api/v1/market/report`
- `/api/v1/risk`
- `/api/v1/scenario/btc`
- `/api/v1/scenario/eth`

## 9. Storage Design

Core tables:

- `market_snapshot`
- `agent_score`
- `prediction_result`
- `risk_result`
- `scenario_result`
- `news_event`
- `market_regime`

The system must preserve historical data for backtesting.
