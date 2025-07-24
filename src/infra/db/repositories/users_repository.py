"""Define the repository for managing user entities in the database."""

from sqlalchemy import select

from src.infra.db.entities.users import Users
from src.infra.db.settings.connection import DBConnectionHandler


class UsersRepository:
	"""Repository for managing user entities in the database."""

	@classmethod
	def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
		"""Insert a new user into the database."""
		with DBConnectionHandler() as database:
			try:
				new_user = Users(first_name=first_name, last_name=last_name, age=age)
				database.session.add(new_user)
				database.session.commit()
			except Exception as e:
				database.session.rollback()
				raise e

	@classmethod
	def get_user(cls, first_name: str, last_name: str, age: int) -> Users:
		"""Retrieve a user by ID from the database."""
		with DBConnectionHandler() as database:
			try:
				user = database.session.execute(
					select(Users).where(
						Users.first_name == first_name,
						Users.last_name == last_name,
						Users.age == age,
					),
				).scalar_one_or_none()
			except Exception as e:
				database.session.rollback()
				raise e
			else:
				return user
