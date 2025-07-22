"""Test for the database connection handler."""

import pytest

from src.infra.db.settings.connection import DBConnectionHandler


@pytest.mark.skip(reason='Sensitive test')
def test_create_database_engine() -> None:
	"""Test the creation of a database engine."""
	db_connection_handler = DBConnectionHandler()
	engine = db_connection_handler.get_engine()

	assert engine is not None
