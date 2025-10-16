"""Define the repository for managing user entities in the database."""

from sqlalchemy import select

from src.data.interfaces.user_repository import UsersRepositoryInterface
from src.domain.model.users import User
from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler


class UsersRepository(UsersRepositoryInterface):
	"""Repository for managing user entities in the database."""

	@classmethod
	def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
		"""Insert a new user into the database."""
		with DBConnectionHandler() as database:
			try:
				new_user = UsersEntity(first_name=first_name, last_name=last_name, age=age)
				database.session.add(new_user)
				database.session.commit()
			except Exception as e:
				database.session.rollback()
				raise e

	@classmethod
	def get_user(cls, first_name: str) -> User:
		"""Retrieve a user by name and age from the database."""
		with DBConnectionHandler() as database:
			try:
				user = database.session.execute(
					select(UsersEntity).where(
						UsersEntity.first_name == first_name,
					),
				).scalar_one_or_none()
			except Exception as e:
				database.session.rollback()
				raise e
			else:
				return user
