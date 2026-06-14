# DATA_SOURCES.md

## 1. Principle

The MVP should use free or low-cost public data sources.

Do not depend on expensive providers such as Glassnode, Nansen, Santiment, Kaiko, or Amberdata for the first version.

## 2. Market Data

### Gate

Use for:

- BTC / ETH price
- futures ticker
- funding rate
- open interest
- order book
- trades
- K-lines

Update frequency:

- price: 1-5 minutes
- funding: 15-60 minutes
- OI: 5-15 minutes
- K-lines: 5-60 minutes

### Binance

Use as secondary market source.

Use for:

- BTC / ETH spot price
- futures price
- volume
- K-lines

Purpose:

- cross-check Gate data
- avoid single-exchange bias

### CoinGecko

Use for:

- market cap
- dominance
- general token metadata

Free tier is acceptable for MVP.

## 3. Macro Data

### FRED

Use for:

- Federal funds rate
- Treasury yields
- macro series

### Public Finance APIs / Yahoo Finance / Stooq

Use for:

- DXY proxy
- Nasdaq
- S&P 500
- VIX if available

Update frequency:

- daily for macro
- hourly or daily for indexes depending on data source

## 4. ETF Data

MVP can start with manually scraped or public table-based ETF flow sources.

Track:

- BTC ETF daily flow
- rolling 3-day net flow
- rolling 7-day net flow
- inflow / outflow streak

For ETH later:

- ETH ETF daily flow
- rolling net flow

## 5. Stablecoin Data

MVP can use CoinGecko or public market cap APIs.

Track:

- USDT market cap
- USDC market cap
- FDUSD market cap
- total stablecoin market cap proxy

Update frequency:

- daily

## 6. News Data

Use RSS feeds when possible.

Suggested sources:

- CoinDesk
- CoinTelegraph
- The Block
- Decrypt
- official SEC news / press releases

MVP logic:

- collect headlines
- classify as BTC / ETH / macro / policy / exchange / ETF
- classify sentiment as bullish / neutral / bearish

## 7. Policy Data

Track:

- SEC announcements
- ETF approval / rejection / delay
- stablecoin regulation
- MiCA updates
- Hong Kong crypto regulation

MVP can rely on news RSS and official website feeds.

## 8. Data Quality Rules

Every collector must store:

- source name
- source URL when applicable
- collection timestamp
- raw payload
- normalized payload
- error status

## 9. Fallback Rules

If a data source fails:

- log error
- preserve latest valid data
- mark `data_freshness` as stale
- reduce prediction confidence

## 10. Data Freshness

Suggested freshness thresholds:

| Data Type | Freshness Threshold |
|---|---|
| Price | 15 minutes |
| OI | 30 minutes |
| Funding | 2 hours |
| ETF | 36 hours |
| Macro | 48 hours |
| Stablecoin | 48 hours |
| News | 12 hours |

If data is stale, the agent must lower confidence.
