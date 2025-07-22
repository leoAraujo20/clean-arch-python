"""Define the repository for managing user entities in the database."""

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
