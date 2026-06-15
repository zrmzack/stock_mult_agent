from datetime import datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import CheckConstraint, DateTime, Index, Integer, JSON, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base
from backend.app.models.mixins import TimestampMixin


class AgentScore(TimestampMixin, Base):
    __tablename__ = "agent_score"
    __table_args__ = (
        CheckConstraint("score >= 0 AND score <= 100", name="ck_agent_score_score_range"),
        CheckConstraint(
            "confidence >= 0 AND confidence <= 1",
            name="ck_agent_score_confidence_range",
        ),
        Index("ix_agent_score_asset_agent_scored_at", "asset", "agent_name", "scored_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    agent_name: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    asset: Mapped[str] = mapped_column(String(16), index=True, nullable=False)
    score: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    trend: Mapped[str] = mapped_column(String(32), nullable=False)
    confidence: Mapped[Decimal] = mapped_column(Numeric(5, 4), nullable=False)
    reasons: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    risks: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    raw_inputs: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    scored_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
