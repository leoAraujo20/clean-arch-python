"""Test for the Users repository."""

from src.infra.db.repositories.users_repository import UsersRepository


def test_insert_user() -> None:
	"""Test the insert_user method of UsersRepository."""
	first_name = 'Test'
	last_name = 'User'
	age = 30
	users_repository = UsersRepository()
	users_repository.insert_user(first_name, last_name, age)
