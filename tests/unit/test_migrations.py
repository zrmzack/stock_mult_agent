from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect

from backend.app.core.config import get_settings


def test_initial_migration_creates_core_tables(tmp_path, monkeypatch) -> None:
    database_url = f"sqlite:///{tmp_path}/migration.db"
    monkeypatch.setenv("DATABASE_URL", database_url)
    get_settings.cache_clear()

    config = Config("alembic.ini")
    command.upgrade(config, "head")

    engine = create_engine(database_url)
    inspector = inspect(engine)

    assert {
        "agent_score",
        "market_regime",
        "market_snapshot",
        "news_event",
        "prediction_result",
        "risk_result",
        "scenario_result",
    }.issubset(set(inspector.get_table_names()))

    command.downgrade(config, "base")
    inspector = inspect(engine)
    assert "agent_score" not in set(inspector.get_table_names())
    get_settings.cache_clear()
