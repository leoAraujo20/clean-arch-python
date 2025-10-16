"""Test for the Users repository."""

from sqlalchemy import select

from src.infra.db.entities.users import Users
from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.settings.connection import DBConnectionHandler


def test_insert_user() -> None:
	"""Test the insert_user method of UsersRepository."""
	first_name = 'Test'
	last_name = 'Insert'
	age = 1
	users_repository = UsersRepository()
	users_repository.insert_user(first_name, last_name, age)

	with DBConnectionHandler() as database:
		user = database.session.execute(
			select(Users).where(
				Users.first_name == first_name,
				Users.last_name == last_name,
				Users.age == age,
			),
		).scalar()
		assert user
		assert user.first_name == first_name
		assert user.last_name == last_name
		assert user.age == age
		database.session.delete(user)
		database.session.commit()

def test_get_user() -> None:
	"""Test the get_user method of UsersRepository."""
	first_name = 'Test'
	last_name = 'Get'
	age = 2
	users_repository = UsersRepository()
	users_repository.insert_user(first_name, last_name, age)
	user = users_repository.get_user(first_name)
	assert user.first_name == first_name
	assert user.last_name == last_name
	assert user.age == age
	with DBConnectionHandler() as database:
		database.session.delete(user)
		database.session.commit()
