import pytest
from sqlalchemy import text

from backend.app.db import session as db_session


def test_build_session_factory_executes_queries(tmp_path) -> None:
    session_factory = db_session.build_session_factory(f"sqlite:///{tmp_path}/session.db")

    with session_factory() as session:
        assert session.execute(text("SELECT 1")).scalar_one() == 1


def test_get_db_closes_session(monkeypatch) -> None:
    class FakeSession:
        closed = False

        def close(self) -> None:
            self.closed = True

    fake_session = FakeSession()
    monkeypatch.setattr(db_session, "SessionLocal", lambda: fake_session)

    generator = db_session.get_db()

    assert next(generator) is fake_session
    with pytest.raises(StopIteration):
        next(generator)
    assert fake_session.closed is True
