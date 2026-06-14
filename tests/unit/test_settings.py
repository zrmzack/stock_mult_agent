from backend.app.core.config import Settings


def test_settings_include_service_urls_from_environment(monkeypatch) -> None:
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql+psycopg://example_user:example_pass@postgres:5432/example_db",
    )
    monkeypatch.setenv("REDIS_URL", "redis://redis:6379/1")

    settings = Settings()

    assert (
        settings.database_url
        == "postgresql+psycopg://example_user:example_pass@postgres:5432/example_db"
    )
    assert settings.redis_url == "redis://redis:6379/1"
