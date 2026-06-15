from datetime import datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import CheckConstraint, DateTime, Index, Integer, JSON, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base
from backend.app.models.mixins import TimestampMixin


class MarketRegime(TimestampMixin, Base):
    __tablename__ = "market_regime"
    __table_args__ = (
        CheckConstraint(
            "confidence >= 0 AND confidence <= 1",
            name="ck_market_regime_confidence_range",
        ),
        Index("ix_market_regime_asset_detected_at", "asset", "detected_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    asset: Mapped[str] = mapped_column(String(16), index=True, nullable=False)
    regime: Mapped[str] = mapped_column(String(64), nullable=False)
    confidence: Mapped[Decimal] = mapped_column(Numeric(5, 4), nullable=False)
    reasons: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    risks: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    raw_inputs: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    detected_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
