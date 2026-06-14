from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, Index, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base
from backend.app.models.mixins import TimestampMixin


class MarketSnapshot(TimestampMixin, Base):
    __tablename__ = "market_snapshot"
    __table_args__ = (
        Index("ix_market_snapshot_asset_collected_at", "asset", "collected_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    asset: Mapped[str] = mapped_column(String(16), index=True, nullable=False)
    source_name: Mapped[str] = mapped_column(String(64), nullable=False)
    source_url: Mapped[str | None] = mapped_column(String(512), nullable=True)
    collected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        index=True,
        nullable=False,
    )
    raw_payload: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    normalized_payload: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )
    data_freshness: Mapped[str] = mapped_column(String(32), default="unknown", nullable=False)
    error_status: Mapped[str | None] = mapped_column(String(128), nullable=True)
