from sqlalchemy import CheckConstraint
from sqlalchemy.schema import CreateTable

from backend.app.db.base import Base
from backend.app.models import (
    AgentScore,
    MarketRegime,
    MarketSnapshot,
    NewsEvent,
    PredictionResult,
    RiskResult,
    ScenarioResult,
)


def test_core_tables_are_registered_in_metadata() -> None:
    assert set(Base.metadata.tables) == {
        "agent_score",
        "market_regime",
        "market_snapshot",
        "news_event",
        "prediction_result",
        "risk_result",
        "scenario_result",
    }


def test_prediction_result_keeps_audit_columns() -> None:
    columns = set(PredictionResult.__table__.columns)

    assert {
        "asset",
        "alpha_score",
        "risk_score",
        "market_regime",
        "prediction",
        "confidence",
        "weights_used",
        "explanations",
        "risk_factors",
        "generated_at",
    }.issubset({column.name for column in columns})


def test_score_models_have_range_constraints() -> None:
    constraint_names = {
        constraint.name
        for table in (
            AgentScore.__table__,
            MarketRegime.__table__,
            PredictionResult.__table__,
            RiskResult.__table__,
        )
        for constraint in table.constraints
        if isinstance(constraint, CheckConstraint)
    }

    assert {
        "ck_agent_score_score_range",
        "ck_agent_score_confidence_range",
        "ck_market_regime_confidence_range",
        "ck_prediction_result_alpha_score_range",
        "ck_prediction_result_risk_score_range",
        "ck_prediction_result_confidence_range",
        "ck_risk_result_risk_score_range",
    }.issubset(constraint_names)


def test_models_compile_to_sql() -> None:
    for model in (
        AgentScore,
        MarketRegime,
        MarketSnapshot,
        NewsEvent,
        PredictionResult,
        RiskResult,
        ScenarioResult,
    ):
        sql = str(CreateTable(model.__table__).compile())
        assert f"CREATE TABLE {model.__tablename__}" in sql
