from datetime import datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import CheckConstraint, DateTime, Index, Integer, JSON, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base
from backend.app.models.mixins import TimestampMixin


class PredictionResult(TimestampMixin, Base):
    __tablename__ = "prediction_result"
    __table_args__ = (
        CheckConstraint(
            "alpha_score >= 0 AND alpha_score <= 100",
            name="ck_prediction_result_alpha_score_range",
        ),
        CheckConstraint(
            "risk_score >= 0 AND risk_score <= 100",
            name="ck_prediction_result_risk_score_range",
        ),
        CheckConstraint(
            "confidence >= 0 AND confidence <= 1",
            name="ck_prediction_result_confidence_range",
        ),
        Index("ix_prediction_result_asset_generated_at", "asset", "generated_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    asset: Mapped[str] = mapped_column(String(16), index=True, nullable=False)
    alpha_score: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    risk_score: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    market_regime: Mapped[str] = mapped_column(String(64), nullable=False)
    prediction: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    confidence: Mapped[Decimal] = mapped_column(Numeric(5, 4), nullable=False)
    weights_used: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    explanations: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    risk_factors: Mapped[list[dict[str, Any]]] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )
    generated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
