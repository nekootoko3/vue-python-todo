import os
from typing import Optional, AsyncIterable

import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy_utils import create_database, database_exists, drop_database
from fastapi.testclient import TestClient

from app.app.main import app
from app.app.database import Base, get_db

TEST_DATABASE_URL = os.environ["TEST_DATABASE_URL"]
engine = create_engine(TEST_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_test_db() -> AsyncIterable[Session]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    """
  Create a clean database on every test case.

  We use the `sqlalchemy_utils` package here for a few helpers in consistently
  creating and dropping the database.
  """
    if database_exists(TEST_DATABASE_URL):
        drop_database(TEST_DATABASE_URL)
    create_database(TEST_DATABASE_URL)  # Create the test database.
    Base.metadata.create_all(bind=engine)  # Create the tables.
    app.dependency_overrides[get_db] = get_test_db  # Mock the Database Dependency
    yield  # Run the tests.
    drop_database(TEST_DATABASE_URL)  # Drop the test database.


@pytest.yield_fixture
def db():
    """Returns an sqlalchemy session, and after the test tears down everything properly."""

    session = Session(bind=engine)

    yield session
    # Drop all data after each test
    for tbl in reversed(Base.metadata.sorted_tables):
        engine.execute(tbl.delete())
    # put back the connection to the connection pool
    session.close()


@pytest.fixture()
def client():
    """
    When using the 'client' fixture in test cases, we'll get full database
    rollbacks between test cases:
    """
    with TestClient(app) as client:
        yield client
