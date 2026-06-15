"""create initial audit schema

Revision ID: 202606150001
Revises:
Create Date: 2026-06-15 00:01:00
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "202606150001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "market_snapshot",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("asset", sa.String(length=16), nullable=False),
        sa.Column("source_name", sa.String(length=64), nullable=False),
        sa.Column("source_url", sa.String(length=512), nullable=True),
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("raw_payload", sa.JSON(), nullable=False),
        sa.Column("normalized_payload", sa.JSON(), nullable=False),
        sa.Column("data_freshness", sa.String(length=32), nullable=False),
        sa.Column("error_status", sa.String(length=128), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_market_snapshot_asset", "market_snapshot", ["asset"])
    op.create_index("ix_market_snapshot_collected_at", "market_snapshot", ["collected_at"])
    op.create_index(
        "ix_market_snapshot_asset_collected_at",
        "market_snapshot",
        ["asset", "collected_at"],
    )

    op.create_table(
        "agent_score",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("agent_name", sa.String(length=64), nullable=False),
        sa.Column("asset", sa.String(length=16), nullable=False),
        sa.Column("score", sa.Numeric(5, 2), nullable=False),
        sa.Column("trend", sa.String(length=32), nullable=False),
        sa.Column("confidence", sa.Numeric(5, 4), nullable=False),
        sa.Column("reasons", sa.JSON(), nullable=False),
        sa.Column("risks", sa.JSON(), nullable=False),
        sa.Column("raw_inputs", sa.JSON(), nullable=False),
        sa.Column("scored_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("score >= 0 AND score <= 100", name="ck_agent_score_score_range"),
        sa.CheckConstraint("confidence >= 0 AND confidence <= 1", name="ck_agent_score_confidence_range"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_agent_score_agent_name", "agent_score", ["agent_name"])
    op.create_index("ix_agent_score_asset", "agent_score", ["asset"])
    op.create_index(
        "ix_agent_score_asset_agent_scored_at",
        "agent_score",
        ["asset", "agent_name", "scored_at"],
    )

    op.create_table(
        "prediction_result",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("asset", sa.String(length=16), nullable=False),
        sa.Column("alpha_score", sa.Numeric(5, 2), nullable=False),
        sa.Column("risk_score", sa.Numeric(5, 2), nullable=False),
        sa.Column("market_regime", sa.String(length=64), nullable=False),
        sa.Column("prediction", sa.JSON(), nullable=False),
        sa.Column("confidence", sa.Numeric(5, 4), nullable=False),
        sa.Column("weights_used", sa.JSON(), nullable=False),
        sa.Column("explanations", sa.JSON(), nullable=False),
        sa.Column("risk_factors", sa.JSON(), nullable=False),
        sa.Column("generated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("alpha_score >= 0 AND alpha_score <= 100", name="ck_prediction_result_alpha_score_range"),
        sa.CheckConstraint("risk_score >= 0 AND risk_score <= 100", name="ck_prediction_result_risk_score_range"),
        sa.CheckConstraint("confidence >= 0 AND confidence <= 1", name="ck_prediction_result_confidence_range"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_prediction_result_asset", "prediction_result", ["asset"])
    op.create_index(
        "ix_prediction_result_asset_generated_at",
        "prediction_result",
        ["asset", "generated_at"],
    )

    op.create_table(
        "risk_result",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("asset", sa.String(length=16), nullable=False),
        sa.Column("risk_score", sa.Numeric(5, 2), nullable=False),
        sa.Column("risk_level", sa.String(length=32), nullable=False),
        sa.Column("risk_factors", sa.JSON(), nullable=False),
        sa.Column("reasons", sa.JSON(), nullable=False),
        sa.Column("raw_inputs", sa.JSON(), nullable=False),
        sa.Column("generated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("risk_score >= 0 AND risk_score <= 100", name="ck_risk_result_risk_score_range"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_risk_result_asset", "risk_result", ["asset"])
    op.create_index("ix_risk_result_asset_generated_at", "risk_result", ["asset", "generated_at"])

    op.create_table(
        "scenario_result",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("asset", sa.String(length=16), nullable=False),
        sa.Column("scenarios", sa.JSON(), nullable=False),
        sa.Column("raw_inputs", sa.JSON(), nullable=False),
        sa.Column("generated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_scenario_result_asset", "scenario_result", ["asset"])
    op.create_index(
        "ix_scenario_result_asset_generated_at",
        "scenario_result",
        ["asset", "generated_at"],
    )

    op.create_table(
        "news_event",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("source_name", sa.String(length=64), nullable=False),
        sa.Column("source_url", sa.String(length=512), nullable=True),
        sa.Column("headline", sa.Text(), nullable=False),
        sa.Column("url", sa.String(length=512), nullable=True),
        sa.Column("category", sa.String(length=64), nullable=True),
        sa.Column("sentiment", sa.String(length=32), nullable=True),
        sa.Column("asset_tags", sa.JSON(), nullable=False),
        sa.Column("raw_payload", sa.JSON(), nullable=False),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_news_event_source_name", "news_event", ["source_name"])
    op.create_index("ix_news_event_published_at", "news_event", ["published_at"])
    op.create_index(
        "ix_news_event_source_collected_at",
        "news_event",
        ["source_name", "collected_at"],
    )

    op.create_table(
        "market_regime",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("asset", sa.String(length=16), nullable=False),
        sa.Column("regime", sa.String(length=64), nullable=False),
        sa.Column("confidence", sa.Numeric(5, 4), nullable=False),
        sa.Column("reasons", sa.JSON(), nullable=False),
        sa.Column("risks", sa.JSON(), nullable=False),
        sa.Column("raw_inputs", sa.JSON(), nullable=False),
        sa.Column("detected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("confidence >= 0 AND confidence <= 1", name="ck_market_regime_confidence_range"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_market_regime_asset", "market_regime", ["asset"])
    op.create_index(
        "ix_market_regime_asset_detected_at",
        "market_regime",
        ["asset", "detected_at"],
    )


def downgrade() -> None:
    op.drop_index("ix_market_regime_asset_detected_at", table_name="market_regime")
    op.drop_index("ix_market_regime_asset", table_name="market_regime")
    op.drop_table("market_regime")

    op.drop_index("ix_news_event_source_collected_at", table_name="news_event")
    op.drop_index("ix_news_event_published_at", table_name="news_event")
    op.drop_index("ix_news_event_source_name", table_name="news_event")
    op.drop_table("news_event")

    op.drop_index("ix_scenario_result_asset_generated_at", table_name="scenario_result")
    op.drop_index("ix_scenario_result_asset", table_name="scenario_result")
    op.drop_table("scenario_result")

    op.drop_index("ix_risk_result_asset_generated_at", table_name="risk_result")
    op.drop_index("ix_risk_result_asset", table_name="risk_result")
    op.drop_table("risk_result")

    op.drop_index("ix_prediction_result_asset_generated_at", table_name="prediction_result")
    op.drop_index("ix_prediction_result_asset", table_name="prediction_result")
    op.drop_table("prediction_result")

    op.drop_index("ix_agent_score_asset_agent_scored_at", table_name="agent_score")
    op.drop_index("ix_agent_score_asset", table_name="agent_score")
    op.drop_index("ix_agent_score_agent_name", table_name="agent_score")
    op.drop_table("agent_score")

    op.drop_index("ix_market_snapshot_asset_collected_at", table_name="market_snapshot")
    op.drop_index("ix_market_snapshot_collected_at", table_name="market_snapshot")
    op.drop_index("ix_market_snapshot_asset", table_name="market_snapshot")
    op.drop_table("market_snapshot")
