# PREDICTION_ENGINE.md

## 1. Goal

Convert multiple agent scores into probability-based outlooks for BTC and ETH.

The engine does not predict exact prices.

It predicts:

- probability of upward movement
- probability of sideways movement
- probability of downward movement

for:

- 3 days
- 7 days
- 14 days

## 2. Input Contract

The prediction engine receives:

```json
{
  "asset": "BTC",
  "market_regime": "bull",
  "regime_confidence": 0.78,
  "agent_scores": {
    "macro": 72,
    "etf": 82,
    "flow": 69,
    "stablecoin": 64,
    "news": 58,
    "policy": 60
  },
  "risk_score": 35
}
```

## 3. Score Normalization

All agent scores must be normalized to 0-100.

Interpretation:

| Score | Meaning |
|---|---|
| 0-40 | Bearish |
| 40-60 | Neutral |
| 60-80 | Bullish |
| 80-100 | Strong bullish |

## 4. Regime-Based Dynamic Weights

Different market regimes require different weights.

### Bull Regime

```yaml
macro: 0.20
etf: 0.30
flow: 0.25
stablecoin: 0.15
news: 0.05
policy: 0.05
```

### Bear Regime

```yaml
macro: 0.30
flow: 0.25
policy: 0.15
etf: 0.15
news: 0.10
stablecoin: 0.05
```

### Sideways Regime

```yaml
flow: 0.35
macro: 0.20
etf: 0.15
news: 0.15
policy: 0.10
stablecoin: 0.05
```

### Risk-Off Regime

```yaml
macro: 0.35
policy: 0.20
flow: 0.20
etf: 0.10
stablecoin: 0.10
news: 0.05
```

### Institution-Driven Regime

```yaml
etf: 0.35
macro: 0.20
flow: 0.20
stablecoin: 0.15
news: 0.05
policy: 0.05
```

## 5. Alpha Score

```text
alpha_score = sum(agent_score * regime_weight)
```

Example:

```text
macro = 72
etf = 82
flow = 69
stablecoin = 64
news = 58
policy = 60
regime = institution_driven

alpha_score = 72*0.20 + 82*0.35 + 69*0.20 + 64*0.15 + 58*0.05 + 60*0.05
alpha_score = 72.4
```

## 6. Probability Mapping

Use a smooth mapping function rather than fixed thresholds.

Recommended first version:

```text
base_up_probability = sigmoid((alpha_score - 50) / 12)
```

Then derive sideways and down probabilities:

```text
up = base_up_probability
risk_adjusted_up = up * (1 - risk_score / 200)
down = (1 - risk_adjusted_up) * risk_bias
sideways = 1 - risk_adjusted_up - down
```

A simple MVP implementation can use calibrated rules:

| Alpha Score | Up | Sideways | Down |
|---|---:|---:|---:|
| < 40 | 25% | 30% | 45% |
| 40-50 | 35% | 40% | 25% |
| 50-60 | 45% | 40% | 15% |
| 60-70 | 58% | 30% | 12% |
| 70-80 | 68% | 22% | 10% |
| > 80 | 76% | 16% | 8% |

## 7. Time Decay

Longer horizons require more uncertainty.

Suggested decay:

```yaml
3d: 1.00
7d: 0.85
14d: 0.70
```

The further the horizon, the closer the distribution should move toward neutral.

Neutral distribution:

```json
{"up": 0.33, "sideways": 0.34, "down": 0.33}
```

Formula:

```text
prob_horizon = neutral * (1 - decay) + prob_3d * decay
```

## 8. Risk Adjustment

Risk score reduces bullish confidence and increases downside probability.

Risk factors include:

- funding overheating
- OI rising too fast
- ETF outflow streak
- DXY sharp rebound
- major macro event within 48 hours
- negative regulatory headline

Risk levels:

| Risk Score | Level |
|---|---|
| 0-30 | Low |
| 30-60 | Medium |
| 60-100 | High |

## 9. Output Contract

```json
{
  "asset": "BTC",
  "alpha_score": 72.4,
  "risk_score": 35,
  "market_regime": "institution_driven",
  "prediction": {
    "3d": {"up": 0.66, "sideways": 0.23, "down": 0.11},
    "7d": {"up": 0.61, "sideways": 0.26, "down": 0.13},
    "14d": {"up": 0.56, "sideways": 0.29, "down": 0.15}
  },
  "confidence": 0.70
}
```

## 10. Backtesting Requirements

Backtest horizons:

- 3 days
- 7 days
- 14 days

Metrics:

- directional accuracy
- Brier score
- calibration curve
- maximum drawdown if used as signal
- precision for high-confidence predictions

Initial target:

- 3-day directional accuracy > 60%
- 7-day directional accuracy > 58%
- 14-day directional accuracy > 55%

Do not claim production value until backtesting exists.
