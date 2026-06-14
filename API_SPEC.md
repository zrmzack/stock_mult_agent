# API_SPEC.md

## 1. Base Path

All APIs use:

```text
/api/v1
```

## 2. Health APIs

### GET /api/v1/health

Response:

```json
{
  "status": "ok",
  "version": "0.1.0"
}
```

## 3. Report APIs

### GET /api/v1/btc/report

Returns full BTC Alpha Report.

Response:

```json
{
  "asset": "BTC",
  "timestamp": "2026-01-01T00:00:00Z",
  "market_regime": "institution_driven",
  "alpha_score": 72.4,
  "risk_score": 35.0,
  "prediction": {
    "3d": {"up": 0.66, "sideways": 0.23, "down": 0.11},
    "7d": {"up": 0.61, "sideways": 0.26, "down": 0.13},
    "14d": {"up": 0.56, "sideways": 0.29, "down": 0.15}
  },
  "drivers": [],
  "risks": [],
  "scenarios": []
}
```

### GET /api/v1/eth/report

Same shape as BTC report. ETH can return `501 Not Implemented` during MVP.

### GET /api/v1/market/report

Returns market-level overview.

## 4. Agent APIs

### GET /api/v1/agents/macro/latest

Returns latest Macro Agent score.

### GET /api/v1/agents/etf/latest

Returns latest ETF Agent score.

### GET /api/v1/agents/flow/latest

Returns latest Flow Agent score.

### GET /api/v1/agents/regime/latest

Returns latest market regime.

Response:

```json
{
  "asset": "BTC",
  "regime": "bull",
  "confidence": 0.78,
  "reasons": []
}
```

## 5. Prediction APIs

### GET /api/v1/prediction/btc

Query parameters:

- `horizon`: optional, values: `3d`, `7d`, `14d`, `all`

### Response

```json
{
  "asset": "BTC",
  "prediction": {
    "3d": {"up": 0.66, "sideways": 0.23, "down": 0.11},
    "7d": {"up": 0.61, "sideways": 0.26, "down": 0.13},
    "14d": {"up": 0.56, "sideways": 0.29, "down": 0.15}
  }
}
```

## 6. Risk APIs

### GET /api/v1/risk/btc

Response:

```json
{
  "asset": "BTC",
  "risk_score": 35,
  "risk_level": "medium",
  "risk_factors": [
    {
      "name": "funding_overheat",
      "severity": "medium",
      "description": "Funding is above normal range."
    }
  ]
}
```

## 7. Scenario APIs

### GET /api/v1/scenario/btc

Response:

```json
{
  "asset": "BTC",
  "scenarios": [
    {
      "name": "Bullish continuation",
      "probability": 0.50,
      "trigger": "ETF inflows continue and DXY remains weak",
      "expected_behavior": "BTC continues upward trend"
    },
    {
      "name": "Sideways consolidation",
      "probability": 0.30,
      "trigger": "ETF inflows slow and derivatives positioning cools",
      "expected_behavior": "BTC ranges sideways"
    },
    {
      "name": "Risk-off pullback",
      "probability": 0.20,
      "trigger": "Macro risk event or negative regulatory headline",
      "expected_behavior": "BTC pulls back"
    }
  ]
}
```

## 8. Data APIs

### GET /api/v1/data/snapshot/latest

Returns latest normalized market snapshot.

### GET /api/v1/data/snapshot/history

Query parameters:

- `asset`
- `start`
- `end`
- `interval`

## 9. Error Format

All errors should use:

```json
{
  "error": {
    "code": "DATA_SOURCE_UNAVAILABLE",
    "message": "Gate API is temporarily unavailable.",
    "details": {}
  }
}
```
