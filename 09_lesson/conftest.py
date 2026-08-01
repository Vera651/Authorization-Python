import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from test_subject import Base

DATABASE_URL = "postgresql://postgres:123@localhost:5432/list"

engine = create_engine(
    DATABASE_URL
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

@pytest.fixture
def db_session():
    """
    Создаёт сессию PostgreSQL для тестов.
    """

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session

    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)