from datetime import datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import CheckConstraint, DateTime, Index, Integer, JSON, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base
from backend.app.models.mixins import TimestampMixin


class RiskResult(TimestampMixin, Base):
    __tablename__ = "risk_result"
    __table_args__ = (
        CheckConstraint(
            "risk_score >= 0 AND risk_score <= 100",
            name="ck_risk_result_risk_score_range",
        ),
        Index("ix_risk_result_asset_generated_at", "asset", "generated_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    asset: Mapped[str] = mapped_column(String(16), index=True, nullable=False)
    risk_score: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    risk_level: Mapped[str] = mapped_column(String(32), nullable=False)
    risk_factors: Mapped[list[dict[str, Any]]] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )
    reasons: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    raw_inputs: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    generated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
