from src.data.interfaces.user_repository import UsersRepositoryInterface
from src.domain.model.users import User


class UsersRepositorySpy(UsersRepositoryInterface):
	"""Spy implementation of UsersRepositoryInterface for testing purposes."""

	def __init__(self) -> None:
		self.insert_user_attributes = {}
		self.get_user_attributes = {}

	def insert_user(self, first_name: str, last_name: str, age: int) -> None:
		"""Mock insert user method."""
		...


	def get_user(self, first_name: str) -> User:
		"""Retrieve mock users by first name."""
		self.get_user_attributes['first_name'] = first_name
		return [
			User(id=1, first_name=first_name, last_name='User', age=30),
            User(id=2, first_name=first_name, last_name='Another', age=25),
        ]
